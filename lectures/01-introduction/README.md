# Lecture 1: Introduction to Language Models

## Learning Objectives
- Understand what language models are and their applications
- Learn the basic architecture of transformers
- Implement a simple attention mechanism

## Content

### What are Language Models?

Language models are statistical models that learn to predict the probability of sequences of words, characters, or tokens. They form the foundation of modern NLP systems.

### Key Concepts

1. **Tokenization**: Breaking text into manageable pieces
2. **Embeddings**: Converting tokens to dense vectors
3. **Attention**: Allowing models to focus on relevant parts of input

### Code Example: Basic Attention

Let's implement a simple attention mechanism to understand the core concept:

```python
import torch
import torch.nn.functional as F

def simple_attention(query, key, value):
    """Simple scaled dot-product attention."""
    # Calculate attention scores
    scores = torch.matmul(query, key.transpose(-2, -1))
    
    # Scale by sqrt of key dimension
    d_k = key.size(-1)
    scores = scores / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    
    # Apply softmax to get attention weights
    attention_weights = F.softmax(scores, dim=-1)
    
    # Apply weights to values
    output = torch.matmul(attention_weights, value)
    
    return output, attention_weights
```

> 📝 **Try it yourself**: Run the code in [`code/attention_demo.ipynb`](./code/attention_demo.ipynb) to see attention in action.

### Interactive Example

The attention mechanism can be visualized as asking questions about a sequence:

1. **Query**: "What should I pay attention to?"
2. **Key**: "Here are the features of each position"  
3. **Value**: "Here's the actual content at each position"

### Exercises

Complete the exercises in the [`exercises/`](./exercises/) directory:

1. **Exercise 1.1**: Implement attention with different scaling factors
2. **Exercise 1.2**: Visualize attention patterns on sample text

### Next Steps

In the next lecture, we'll dive deeper into tokenization and see how different tokenization strategies affect model performance.

---

**Navigation:**
- [← Course Home](../../README.md)
- [Next: Tokenization →](../02-tokenization/README.md)
