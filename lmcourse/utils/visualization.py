"""Visualization utilities for language models."""

import matplotlib.pyplot as plt
import seaborn as sns
import torch
import numpy as np
from typing import Optional


def plot_attention_heatmap(
    attention_weights: torch.Tensor,
    tokens: Optional[list[str]] = None,
    title: str = "Attention Weights",
    figsize: tuple[int, int] = (10, 8)
) -> None:
    """Plot attention weights as a heatmap.
    
    Args:
        attention_weights: Tensor of shape [seq_len, seq_len] or [batch, seq_len, seq_len]
        tokens: Optional list of token strings for axis labels
        title: Plot title
        figsize: Figure size tuple
    """
    # Handle batch dimension
    if attention_weights.dim() == 3:
        attention_weights = attention_weights[0]
    
    weights_np = attention_weights.detach().cpu().numpy()
    
    plt.figure(figsize=figsize)
    
    # Create labels
    if tokens is None:
        labels = [f"Pos {i}" for i in range(weights_np.shape[0])]
    else:
        labels = tokens[:weights_np.shape[0]]  # Truncate if needed
    
    sns.heatmap(
        weights_np,
        annot=True,
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels,
        fmt=".3f"
    )
    
    plt.title(title)
    plt.xlabel("Keys")
    plt.ylabel("Queries")
    plt.tight_layout()
    plt.show()


def plot_token_embeddings(
    embeddings: torch.Tensor,
    tokens: list[str],
    method: str = "pca"
) -> None:
    """Plot 2D visualization of token embeddings.
    
    Args:
        embeddings: Token embeddings of shape [vocab_size, embed_dim]
        tokens: List of token strings
        method: Dimensionality reduction method ("pca" or "tsne")
    """
    from sklearn.decomposition import PCA
    from sklearn.manifold import TSNE
    
    embeddings_np = embeddings.detach().cpu().numpy()
    
    if method == "pca":
        reducer = PCA(n_components=2)
    elif method == "tsne":
        reducer = TSNE(n_components=2, random_state=42)
    else:
        raise ValueError(f"Unknown method: {method}")
    
    embeddings_2d = reducer.fit_transform(embeddings_np)
    
    plt.figure(figsize=(12, 8))
    plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], alpha=0.7)
    
    for i, token in enumerate(tokens):
        plt.annotate(token, (embeddings_2d[i, 0], embeddings_2d[i, 1]))
    
    plt.title(f"Token Embeddings ({method.upper()})")
    plt.xlabel(f"{method.upper()} Component 1")
    plt.ylabel(f"{method.upper()} Component 2")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_loss_curves(
    train_losses: list[float],
    val_losses: Optional[list[float]] = None,
    title: str = "Training Progress"
) -> None:
    """Plot training and validation loss curves.
    
    Args:
        train_losses: List of training losses per epoch
        val_losses: Optional list of validation losses per epoch
        title: Plot title
    """
    plt.figure(figsize=(10, 6))
    
    epochs = range(1, len(train_losses) + 1)
    plt.plot(epochs, train_losses, 'b-', label='Training Loss', linewidth=2)
    
    if val_losses is not None:
        plt.plot(epochs, val_losses, 'r-', label='Validation Loss', linewidth=2)
    
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# Private helper function - not exported in __init__.py
def _normalize_attention_for_display(attention_weights: torch.Tensor) -> torch.Tensor:
    """Normalize attention weights for better visualization."""
    return torch.softmax(attention_weights, dim=-1)