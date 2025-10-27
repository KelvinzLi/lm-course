"""Learning rate schedulers."""

import math

import torch
from torch.optim.lr_scheduler import LambdaLR

def get_cos_with_warmup(
    optimizer: torch.optim.Optimizer,
    num_warmup_steps: int,
    num_training_steps: int,
    min_lr_ratio: float = 0.1,
    num_cycles: float = 0.5,
    last_epoch: int = -1,
) -> LambdaLR:
    """Learning rate scheduler that linearly increases the learning rate from 0.0 to the initial lr over
    after ``num_warmup_steps``, then decreases to `min_lr` on a cosine schedule
    over the remaining steps.
    """

    def lr_lambda(current_step: int) -> float:
        # Linear warmup phase
        if current_step < num_warmup_steps:
            return current_step / max(1, num_warmup_steps)
        # Cosine decay phase
        progress = (current_step - num_warmup_steps) / max(
            1, num_training_steps - num_warmup_steps
        )
        # This is the original cosine wave that goes from 1.0 to 0.0
        cosine_wave = 0.5 * (1.0 + math.cos(math.pi * num_cycles * 2.0 * progress))
        # Rescale the wave to go from 1.0 to min_lr_ratio
        lr_multiplier = min_lr_ratio + (1.0 - min_lr_ratio) * cosine_wave
        return lr_multiplier

    return LambdaLR(optimizer, lr_lambda, last_epoch)
