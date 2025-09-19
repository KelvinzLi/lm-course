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
lectures/           # Main course content
├── 01-introduction/        # Language models overview & attention
├── 02-tokenization/        # Text preprocessing & subword methods  
├── 03-embeddings/          # Word vectors & positional encoding
├── 04-transformers/        # The transformer architecture
├── 05-training/           # Optimization & scaling
├── 06-pretrained-models/  # GPT, BERT, T5 families
├── 07-fine-tuning/        # Task-specific adaptation
├── 08-generation/         # Decoding strategies & sampling
├── 09-evaluation/         # Metrics & benchmarks
└── 10-advanced/           # RLHF, agents, & latest research

assignments/        # Major projects
├── assignment-1/          # Implement attention from scratch
├── assignment-2/          # Build a mini-GPT
├── assignment-3/          # Fine-tune for specific task
└── final-project/         # Open-ended research project

lmcourse/          # Shared utilities and reference implementations
resources/         # Papers, datasets, and additional materials
```

## 🚀 Quick Start

1. **Setup Environment**
   ```bash
   git clone https://github.com/yourusername/lm-course.git
   cd lm-course
   uv sync
   ```

2. **Start Learning**
   - Read the [Setup Guide](docs/SETUP.md)
   - Begin with [Lecture 1: Introduction](lectures/01-introduction/README.md)
   - Follow along with code examples and exercises

3. **Get Help**
   - 🛠️ [Setup Instructions](docs/SETUP.md) 
   - 💬 [GitHub Discussions](../../discussions)
   - 🐛 [Report Issues](../../issues)

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

See [Contributing Guide](docs/CONTRIBUTING.md) for details.

## 📄 License

This course is released under [MIT License](LICENSE). Feel free to use, modify, and share!

## 🙏 Acknowledgments

- Inspired by CS224N, CS25, and other excellent NLP courses
- Built on top of 🤗 Transformers, PyTorch, and the open-source ML community
- Thanks to all contributors and students who help improve this course

---

**Ready to dive in?** Start with [Lecture 1: Introduction to Language Models](lectures/01-introduction/README.md) 🚀