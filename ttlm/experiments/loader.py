"""Experiment configuration loading."""

from ttlm.config import PreTrainingConfig


def load(
    experiment: str, experiment_id: int | None = None
) -> PreTrainingConfig | list[PreTrainingConfig]:
    """Load experiment config by name and optional index.

    Returns either a single config or indexed config from a sweep.
    """
    try:
        module = __import__(f"experiments.{experiment}", fromlist=["CFG"])
    except ModuleNotFoundError:
        raise ValueError(f"Experiment '{experiment}' not found")

    config = module.CFG
    if not isinstance(config, list):
        config = [config]

    if experiment_id >= len(config):
        raise ValueError(
            f"Experiment ID {experiment_id} out of range (0-{len(config) - 1})"
        )
    config = config[experiment_id]

    return config