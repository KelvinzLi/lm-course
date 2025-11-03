# Language Models Course

A simple, hands-on course on language models. Learn by doing.

## Quick Start (Local Setup)

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone https://github.com/yourusername/lm-course.git
cd ttlm
uv sync

# Start learning
uv run python -m scripts.pretrain --experiment=default (or any other experiment, like default_cpu for cpu only job)


## Using Google Colab

1. Open a new notebook on colab and start a new runtime (GPU or CPU, recommended GPU)
2. Run the following code in a cell: 

```python



## Course Structure


```
lm-course/
├── notes/          # Lecturer's notes
└── ttlm/          # Code and utilities
```

## Lectures

A full manuscript with notes is being prepared. For now, you can find some slides that will support our discussion in [notes](notes/ttlm_support.pdf).

1. **Introduction** - Language modeling
2. **Tokenization** - Text preprocessing
3. **Embeddings** - Word vectors
4. **Transformers** - Core architecture
5. **Pretraining** - How to pretrain models
8. **Generation** - Text generation strategies

## Prerequisites

- Python/torch programming
- Basic linear algebra
- Some familiarity and previous experience with neural networks (helpful)

## License

MIT License - use freely!

---
