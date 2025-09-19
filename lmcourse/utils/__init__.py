"""Utility functions for the LM course."""

from .visualization import (
    plot_attention_heatmap, 
    plot_token_embeddings,
    plot_loss_curves,
)

__all__ = [
    "plot_attention_heatmap",
    "plot_token_embeddings", 
    "plot_loss_curves",
    # Note: _normalize_attention_for_display is NOT exported (private helper)
]
