# COSC 426 F25 Lab 6

## Introduction

In this lab you will work with `GLoVe` and `distilgpt` word embeddings. Concretely, you will use the similarity between different words to reason about what information is encoded in these embeddings. 

This lab has three required parts, and one optional part. 

* Part 1: Computing similarity between `GLoVe` embeddings
* Part 2: Computing similarity between `distilgpt` embeddings
* Part 3: Using analogies to study encoding of gender
* Part 4 (optional): Using analogies to study encoding of other features

### Grading
In order to get the `Meets Expectation` designation for this lab, you should correctly complete the first three parts. To get the `Exceeded Expectation` designation you should also correctly complete part 4. 

### Provided files

- `glove_dolma_300_10k.pkl`: the 300-dimensional [GLoVe word embeddings](https://nlp.stanford.edu/projects/glove/) trained on 220B tokens. The original file had embeddings for 1.2M words, but this file includes the embedding for only 10k  most frequent words, with frequency measured using [CoCA](https://www.english-corpora.org/coca/).  

- `Lab6.ipynb`: the file where you will implement all functions, and run all experiemnts. 

### What to submit

- `Lab6.ipynb` with the code implemented and answers to questions in each part


## Part 1: Computing similarity between `GLoVe` embeddings

In this part you should first familiarize yourself with how to work with word GLoVe embeddings. Once you've done this, you should implement and test the following functions: 

* `get_glove_wordvec(word, embeddings)`
* `cosine_similarity(vec1, vec2)`. **To make your code efficient, you should use numpy vector/matrix operations, and not for loops**
* `find_similar(word_vec, n, embeddings)`

After you've implemented this, you should answer the following questions about the `find_similar` function: 

1. What is the time complexity of `find_similar` if your vocab has `v` words, your embedding size is `m`, and you want to find `n` most similar words to the inputted word? 

2. Consider a scenario (e.g., web application that displays similar words) where you might have to repeatedly run `find_similar`, say for `x` times. What are the benefits and challenges of pre-computing the similarity between all words? How might you overcome the challenges? 

## Part 2: Computing similarity between `distilgpt` embeddings  


In this part you should: 

1. Familiarize yourself with how to work with word embeddings of  `distilgpt` (and more broadly transformer LMs on Huggingface). Answer the following question: How does `distilgpt` handle words that are not in its vocab? 

2. Implement `get_hf_wordvec(word, tokenizer, embedding_matrix)` 

3. Explain: What are the limitations of using `embedding_matrix` in `find_similar`? 

4. Implement `create_hf_embeddings(hf_model_name, vocab)`


## Part 3: Using analogies to study encoding of gender

[Mikolov et al](https://arxiv.org/abs/1301.3781) proposed a method of investigating the relationship between word vectors using analogies: subtract two words and add in the third word, and find the most similar (or n most similar) words to the new embedding. The classic example is to check whether the vector closes to `king - man + woman`  is `queen`. 

In this part you should: 

1. Implement and test `compute_analogy(analogy, embeddings, n)` 

2. Come up with at least 10 analogies that you think are important for testing how robustly gender is encoded in some embeddings. Justify why you picked the examples you did. 

3. Use `compute_analogy` and your analogies to test how robustly gender is encoded in `GLoVe` and `distilgpt` embeddings. 

## Part 4 (Optional): Using analogies to study encoding of other features

For this part, do the following: 

1. Pick a feature (or more!) that you think should be encoded in a good word embedding. Justify why you think this is a useful feature. 

2. Repeat experiment from Part 3 for your feature and discuss whether you think the feature is encoded in `GLoVe` and `distilgpt` embeddings. 

3. Discuss: How useful do you think similarity or analogies are in evaluating word embeddings? Are there any limits on the kind of features you can probe? 


