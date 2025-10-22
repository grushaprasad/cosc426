# COSC 426 F25 Lab 7

## Introduction

In this lab you will use pytorch to implement a neural network model that can learn word embeddings. Concretely, you will use the the contextual bag of words modeling setup we discussed in class. 

**Note: this lab does not assume any prior pytorch experience, but assumes that you will be able to look things up, ask questions, and learn as you go!**

This lab has three required parts and one optional part. 

* Part 1: Familiarize yourself with the different components of the CBOW model 

* Part 2: Train and evaluate a CBOW model on toy data, and explore the word embeddings. 

* Part 3: Explore the role of training data on the word embeddings that are learned

* Part 4 (optional): Explore the role of other factors on the word embeddings that are learned

### Grading
In order to get the `Meets Expectation` designation for this lab, you should correctly complete the first three parts. To get the `Exceeded Expectation` designation you should also correctly complete part 4. 

### Provided files

- `CBOW.py`: the file which has all of the classes required to train and evaluate a CBOW model

- `Lab7.ipynb`: the file where you will run all the experiments and answer all the questions

- `data`: the folder with all of the rquired toy and real data

### What to submit

- `Lab7.ipynb` with the code implemented and answers to questions in each part

- `CBOW2.py` (optional): the file with a new model architecture if you choose to build one for part 4. 

## Part 1: Familiarize yourself with the different components of the CBOW model 

There are four components involved in training and evaluating a model, each associated with a class in `CBOW.py`. In this part your goal is to read through the code and answer the questions. 

**Verify your answers with me after each sub-part!**

### Part 1.1: The dataset

1. Create a `CBOW_Dataset` object with `sample_alice.txt`, `sample_vocab.txt`, and a window size of 4. How many training examples does the dataset have? (*Hint: Remember you can access the variables in the object's init*)

2. Create a `CBOW_Dataset` object with `sample_alice.txt`, `sample_vocab.txt`, and a window size of 2. How many training examples does the dataset have?

3. Does window size affect the number of training examples, why or why not? 

4. What does one training example look like? What is the sequence of steps to go from text in the form of a string to the final format and data types of the training example? 

5. Is this final dataset case-sensitive (i.e., does it treat lower and upper case differently)? If it is, how can you change it to not be case-sensitive and vice versa? 

### Part 1.2: The model architecture

1. In the `__init__` part of the `CBOW_Model`, you are initializing a `torch.nn.Embedding` layer. Conceptually, what does this layer do? What are the input and output dimensions of this layer? Why does this make sense?

2. You are also initializing a `torch.nn.Linear` layer. Conceptually, what does this layer do? What are the input and output dimensions of this layer? Why does this make sense? 

2. Describe in your own words what you think is happening in the `forward` function. 

3. Describe in your own words what you think is happening in the `loss` function.


### Part 1.3: The trainer

1. When you create a `CBOW_Trainer` object, you also have to pass in the following parameters. Explain how these paramters are used during training? 
* `num_epochs`
* `lr`
* `batch_size` 
* `train_data`
* `val_data`
* `device`


2. We are loading training data using `torch.utils.data.DataLoader`. What are the parameters for this function? What is the format in which this function returns the data? 

3. The following line calls the `forward` function of the model and saves the output. 
```
y_pred = model(X)
```
Describe what you think each of the following lines are doing. 
* `X,y_target = X.to(self.device), y_target.to(self.device)`
* `loss = model.loss(y_pred, y_target)`
* `optimizer.zero_grad()`
* `loss.backward()`
* `optimizer.step()`



### Part 1.4: The evaluator

1. Describe what `compute_loss` and `get_preds` do. Which of these two functions is closest to the evaluate mode in `NLPScholar`?

2. Why do these functions have `@torch.nograd`?

3. Say you have a `CBOW_Model` object `model`, and a `CBOW_Dataset` object called `test_data`. How will you use this class to calculate the loss of `model` on `test_data`? 

## Part 2: Train and evaluate a CBOW model on toy data, and explore the word embeddings. 

In this part, you will put all of the components together to train and evaluate a toy model. The instructions for this part are deliberately a little vague beecause the goal is for you to figure out how to use the `CBOW` model. 

You will use following files:

* Training data: `sample-alice.txt`
* Validation data: `sample-lookingglass.txt`
* Vocab: `sample_vocab.txt`

Concretely, you will do the following:

1. Intialize a toy model with embedding size of 50.
2. Report the randomly initialized model's loss and accuracy on the training data. 
3. You can get the model's randomly initialized embedding matrix with `embedding_matrix = cbow_model.embed.weight.data`. Use this matrix to compute the cosine similarity between the following pairs. (*Hint: think about how you approached this with `distilgpt` in Lab6*) 
    * think-thought
    * think-tired
    * sleepy-thought
    * sleepy-tired 
4. Train the model on 1000 epochs with batch size 8 and a learning rate of 0.5
5. Report the trained model's loss and accuracy. 
6. Repeat step 3, but now with the embedding matrix of the trained model. 
7. Do you think that the model has learned the task? Do you think the model has learned useful embeddings? 
8. Last lab we used word vectors with 300 dimensions. Does it make sense to use embedding size of 300 for this toy data? Why or why not? 


## Part 3: Explore the role of training data on the word embeddings that are learned

In this part, you will do the following: 

1. Train two CBOW models with embedding size 100 for at least 50 epochs with learning rate of 0.1, one each on `alice_in_wonderland.txt` and `sherlock_holmes_short.txt`. For the vocab, use `coca_vocab_10k.txt`, which has the 10k most frequent words as estimated from COCA. Since we are not evaluating model generalization, you can use the training file as the validation file. **Save the two models using `torch.save` so that you are able to load the trained model even if your session ends**. 

2. Come up with a list of (at least) 10 words in the vocabulary that you think will have the same learned embeddings across the texts. Justify why you think the embeddings will be similar. 

3. Come up with a list of (at least) 10 words in the vocabulary that you think will have more varied learned embeddings across the texts relative to the list in the previous question. Justify why you think the embeddings will be varied.

4. Test your hypotheses by comparing the embeddings of words in each list between the two CBOW models. 


## Part 4 (optional): Explore the role of other factors on the word embeddings that are learned

For this part do the following: 

1. Pick (at least) one of the following factors that could impact learned word embeddings: 
* Context size 
* Embedding size 
* Model architecture (e.g., adding another layer)

2. Come up with a way to measure goodness of the learned word embeddings, and justify this. (*Hint: some ideas are to use similarities between specific words, analogies, etc*)

3. Systematically vary the factor that you picked, and evaluate whether this factor changes the goodness of the learned representations for either the alice or sherlock text, and discuss your results. 


Note: Training the model on the `glove_10k` vocab on the full texts can take time. So here are some alternatives to speed up training: 

1. Create a python script to submit jobs on Turing (e.g., one job per parameter setting). You will also be able to use GPUs. 

2. Define a smaller vocabulary size and justify why you picked this smaller set. 

