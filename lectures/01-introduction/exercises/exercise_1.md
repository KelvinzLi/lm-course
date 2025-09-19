# Exercise 1: Understanding Attention

## Part A: Implement Attention Variants

1. **Multi-Head Attention**: Extend the simple attention to use multiple attention heads
2. **Masked Attention**: Implement causal masking for autoregressive models
3. **Cross Attention**: Implement attention between two different sequences

## Part B: Analysis Questions

1. What happens to attention patterns when you change the scaling factor?
2. How do random vs. structured query/key matrices affect attention distribution?
3. Why is the softmax function crucial for attention weights?

## Part C: Coding Challenge

Implement a function that visualizes attention patterns for the sentence:
"The cat sat on the mat"

Requirements:
- Tokenize the sentence
- Create meaningful embeddings (you can use random but consistent embeddings)
- Visualize which words attend to which other words
- Explain the patterns you observe

## Submission

Create a Jupyter notebook with your solutions and explanations. Include:
- Working code for all implementations
- Visualizations of attention patterns
- Written explanations of your observations

**Due**: Before next lecture

**Help**: Check the [solutions](./solutions/) directory after attempting the exercises yourself.
