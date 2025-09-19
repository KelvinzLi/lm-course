# Language Models Course

A comprehensive, hands-on course on language models covering theory, implementation, and practical applications. This course takes you from basic concepts to state-of-the-art transformer architectures.

## 🎯 Course Overview

This course is designed for students and practitioners who want to understand how modern language models work. Each lecture combines theoretical concepts with practical coding exercises, building up to implementing your own transformer from scratch.

### What You'll Learn

- **Fundamentals**: Tokenization, embeddings, and attention mechanisms
- **Architectures**: Transformers, GPT, BERT, and modern variants
- **Training**: Optimization, scaling laws, and distributed training
- **Applications**: Fine-tuning, prompting, and deployment strategies
- **Latest Research**: RLHF, instruction tuning, and emerging techniques

## 📚 Course Structure

```
lm-course/
├── lectures/               # Main course content
│   ├── 01-introduction/    # Language models overview & attention
│   ├── 02-tokenization/    # Text preprocessing & subword methods  
│   ├── 03-embeddings/      # Word vectors & positional encoding
│   ├── 04-transformers/    # The transformer architecture
│   ├── 05-training/        # Optimization & scaling
│   ├── 06-pretrained-models/  # GPT, BERT, T5 families
│   ├── 07-fine-tuning/     # Task-specific adaptation
│   ├── 08-generation/      # Decoding strategies & sampling
│   ├── 09-evaluation/      # Metrics & benchmarks
│   └── 10-advanced/        # RLHF, agents, & latest research
└── lmcourse/               # Course package
    ├── utils/              # Visualization, data loading
    ├── models/             # Reference implementations
    ├── datasets/           # Sample data and loaders
    └── assignments/        # Project templates and solutions
```

## 🚀 Quick Start

```bash
# 1. Install UV (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.zshrc  # or restart your terminal

# 2. Clone and setup course
git clone https://github.com/yourusername/lm-course.git
cd lm-course
uv sync

# 3. Start learning!
uv run jupyter notebook
```

**That's it!** 🎉 You're ready for [Lecture 1: Introduction](lectures/01-introduction/README.md).

<details>
<summary>📖 Alternative Installation (pip/conda)</summary>

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

### **Verification**
```bash
# Test course setup
uv run python -c "from lmcourse.utils import plot_attention_heatmap; print('✅ Course ready!')"
```

### **🐛 Troubleshooting**
- **"No module named 'lmcourse'"**: Run `uv sync` (or `pip install -e .`)
- **ImportError in notebooks**: Restart Jupyter kernel
- **Out of memory**: Use Google Colab or reduce batch sizes

## 🎓 Prerequisites

- **Programming**: Intermediate Python (familiarity with NumPy)
- **Math**: Linear algebra, basic calculus, probability
- **ML Background**: Basic understanding of neural networks (helpful but not required)

## 📋 Syllabus

| Week | Topic | Lectures | Assignments |
|------|--------|----------|-------------|
| 1-2  | Foundations | Introduction, Tokenization, Embeddings | Implement attention |
| 3-4  | Core Architecture | Transformers, Training | Build mini-GPT |
| 5-6  | Pretrained Models | GPT/BERT families, Fine-tuning | Task-specific tuning |
| 7-8  | Advanced Topics | Generation, Evaluation | Research project |
| 9-10 | Current Research | RLHF, Agents, Latest papers | Final presentations |

## 🏆 Learning Outcomes

By the end of this course, you will be able to:

- [ ] Implement transformer architectures from scratch
- [ ] Train and fine-tune language models effectively  
- [ ] Understand the trade-offs in model design and scaling
- [ ] Apply LMs to real-world NLP tasks
- [ ] Critically evaluate current research and identify future directions

## 📖 Recommended Readings

**Essential Papers** (covered in lectures):
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - The Transformer
- [BERT](https://arxiv.org/abs/1810.04805) - Bidirectional representations
- [GPT-3](https://arxiv.org/abs/2005.14165) - Large-scale language models

**Textbooks**:
- [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) - Jurafsky & Martin
- [Natural Language Processing with Transformers](https://transformersbook.com/) - Tunstall et al.

## 🤝 Contributing

This is an open-source educational resource! Contributions welcome:

- 🐛 **Bug Reports**: Found an error? Open an issue
- 💡 **Improvements**: Better explanations or code examples
- 📚 **Content**: Additional exercises or advanced topics
- 🌍 **Translations**: Help make this accessible worldwide

<details>
<summary>🛠️ Development Setup</summary>

```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.zshrc  # or restart terminal

# Clone and setup
git clone https://github.com/yourusername/lm-course.git
cd lm-course
uv sync --group dev  # Installs dev tools (pytest, black, flake8)
```

**Adding Dependencies:**
```bash
uv add package-name              # Automatically updates pyproject.toml
uv add --group dev tool-name     # For development tools
```

**Code Quality:**
```bash
uv run black .                   # Format code
uv run flake8 lmcourse/         # Check style
uv run pytest --nbval lectures/ # Test notebooks execute properly
```

**Adding New Utilities:**
1. Create function in appropriate module (e.g., `lmcourse/utils/visualization.py`)
2. Export in module `__init__.py` if it's public API
3. Add to package level only if used in 3+ lectures

**Coding Standards:**
- Procedural, C-like code style
- Type hints for all functions
- Short functions (<50 statements)
- Snake_case naming
- Docstrings for public functions

</details>

## 📄 License

This course is released under [MIT License](LICENSE). Feel free to use, modify, and share!

## 🙏 Acknowledgments

- Inspired by CS224N, CS25, and other excellent NLP courses
- Built on top of 🤗 Transformers, PyTorch, and the open-source ML community
- Thanks to all contributors and students who help improve this course

---

**Ready to dive in?** Start with [Lecture 1: Introduction to Language Models](lectures/01-introduction/README.md) 🚀