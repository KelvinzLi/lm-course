"""Distributed training utilities for PyTorch."""
""" Original author: Liam Atkinson """

import os
from contextlib import AbstractContextManager
from dataclasses import dataclass, field
from datetime import timedelta
from types import TracebackType
from typing import ClassVar, Literal

import torch
import torch.distributed as dist


@dataclass(slots=True)
class World(AbstractContextManager):
    """Minimal but tidy context manager for `torch.distributed`."""

    device: torch.device | str = "cpu"
    backend: Literal["nccl", "gloo", "mpi"] | None = None
    timeout_sec: int = 1800

    _ENV_KEYS: ClassVar[tuple[str, ...]] = (
        "RANK",
        "WORLD_SIZE",
        "MASTER_ADDR",
        "MASTER_PORT",
    )

    timeout: timedelta = field(init=False)
    rank: int = field(init=False, default=0)
    world_size: int = field(init=False, default=1)
    local_rank: int = field(init=False, default=0)

    @property
    def distributed(self) -> bool:
        """True ↔ a process group exists and spans > 1 process."""
        return dist.is_initialized() and self.world_size > 1

    @property
    def is_main_process(self) -> bool:
        """Return true if this is the main process."""
        return self.rank == 0

    def __post_init__(self) -> None:
        """Convert and validate constructor arguments."""
        self.timeout = timedelta(seconds=self.timeout_sec)
        self.device = torch.device(self.device)

        if self.device.type == "cuda" and not torch.cuda.is_available():
            raise RuntimeError("CUDA device requested but CUDA is not available")

    def __enter__(self) -> "World":
        """Enter the distributed context."""
        if self._should_init_pg():
            dist.init_process_group(
                backend=self.backend or self._auto_backend,
                timeout=self.timeout,
            )

        self.rank = dist.get_rank() if dist.is_initialized() else 0
        self.world_size = dist.get_world_size() if dist.is_initialized() else 1
        self.local_rank = int(os.getenv("LOCAL_RANK", self.rank))

        if self.device.type == "cuda":
            if self.local_rank >= torch.cuda.device_count():
                raise RuntimeError(
                    f"Local rank {self.local_rank} exceeds visible CUDA devices "
                    f"({torch.cuda.device_count()}). Check CUDA_VISIBLE_DEVICES."
                )
            torch.cuda.set_device(self.local_rank)
            self.device = torch.device(f"cuda:{self.local_rank}")

        return self

    def barrier(self) -> None:
        """Synchronise all processes. No-op in single-process runs."""
        if self.distributed:
            dist.barrier()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        """Exit the distributed context."""
        if dist.is_initialized():
            dist.destroy_process_group()

    @staticmethod
    def _should_init_pg() -> bool:
        """Return True only when the standard env vars are set *and* WORLD_SIZE>1."""
        if any(k not in os.environ for k in World._ENV_KEYS):
            return False
        return int(os.getenv("WORLD_SIZE", "1")) > 1

    @property
    def _auto_backend(self) -> str:
        """Pick a sensible default backend from the current device."""
        return "nccl" if self.device.type == "cuda" else "gloo"
