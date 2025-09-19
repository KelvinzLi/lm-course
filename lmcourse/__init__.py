"""LM Course - Language Models Course utilities and implementations."""

__version__ = "0.1.0"
__author__ = "Your Name"

# Make key utilities available at package level
from .utils import plot_attention_heatmap, plot_token_embeddings

__all__ = [
    "plot_attention_heatmap", 
    "plot_token_embeddings",
]
