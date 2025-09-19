# Course Setup Guide

## Quick Start (Recommended)

```bash
# 1. Install UV (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.zshrc  # or restart your terminal

# 2. Clone and enter directory
git clone https://github.com/yourusername/lm-course.git
cd lm-course

# 3. Install with UV (automatic dependency management)
uv sync

# 4. Start learning!
uv run jupyter notebook
```

**That's it!** 🎉 You're ready to start with [Lecture 1](../lectures/01-introduction/README.md).

---

## Alternative Installation Methods

### Option B: Traditional pip/conda

<details>
<summary>Click to expand pip/conda instructions</summary>

#### Using conda:
```bash
conda create -n lm-course python=3.9
conda activate lm-course
cd lm-course
pip install -e .
jupyter notebook
```

#### Using venv:
```bash
python -m venv lm-course-env
source lm-course-env/bin/activate  # Windows: lm-course-env\Scripts\activate
cd lm-course
pip install -e .
jupyter notebook
```

</details>

---

## Verification

### With UV:
```bash
uv run python -c "from lmcourse.utils import plot_attention_heatmap; print('✅ Course ready!')"
```

### With pip/conda:
```bash
python -c "from lmcourse.utils import plot_attention_heatmap; print('✅ Course ready!')"
```

---

## GPU Setup (Optional)

- **Google Colab**: No setup needed - just upload notebooks
- **Local NVIDIA GPU**: PyTorch auto-detects CUDA
- **Apple Silicon**: MPS backend included automatically

---

## Troubleshooting

### "No module named 'lmcourse'"
```bash
# With UV:
uv sync

# With pip:
pip install -e .
```

### "ImportError" in notebooks
Restart your Jupyter kernel after installation.

### Out of memory
Use Google Colab for GPU access or reduce batch sizes in examples.

---

## For Contributors

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and coding guidelines.