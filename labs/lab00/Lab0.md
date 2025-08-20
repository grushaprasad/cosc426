# COSC 426 F25 Lab 0

## Introduction

This "lab" is intended to be completed before the first official lab on September 3rd 2025. There are three parts to this lab: 

1. Intalling required software on your personal computer
2. Installing required software on Turing, Colgate's HPC. 
3. Python refresher

**Please don't hesitate to reach out if you are stuck! It is very important that you finish this before the first lab**

## Part 1: Installation on your personal computer

In this class, you will be using the [NLPScholar toolkit](https://github.com/forrestdavis/NLPScholar/) that Prof. Forrest Davis and I co-developed. The goal of this part is to ensure that you are setup to use the toolkit before the first lab. 

#### Step 1: Clone the `NLPScholar` repository. 

1. Open the command line interface on your computer. (If you are unfamiliar with using the command line, here is [a helpful video](https://www.youtube.com/watch?v=bE9DyH43C2I), and here is [a cheatsheet](https://www.geeksforgeeks.org/linux-unix/linux-vs-windows-commands/) of different commands for Linux and Windows.)

2. Navigate to the folder where you want to have all of the work for this class. (I would also recommend you create separate folders for labs and HWs)

3. Type `git clone https://github.com/forrestdavis/NLPScholar.git` (You can find this link for any Github repository by going to the repository on Github, clicking the green `Code` button and copying the HTTPs link)


#### Step 2: Set up the `conda` environment.

Follow the instructions in [Install.md](https://github.com/forrestdavis/NLPScholar/blob/main/Install.md) on the repository to setup the `nlp` environment. If you run into errors, make sure to read the troubleshooting section. You can ignore the parts about Turing at this point in the lab. 

To verify that your setup worked correctly: 

1. Activate the conda environment
2. Open a python shell by typing `python`
3. Try to import each of the packages listed in [environment.yml](https://github.com/forrestdavis/NLPScholar/blob/main/environment.yml). For example, if you want to verify that `accelerate` was installed correctly, you would type `import accelerate`. 


#### Step 3: Test NLPScholar installation

1. Navigate to the `NLPScholar` repository on your computer
2. Activate the `nlp` environment (if it isn't already active)
3. Run `python main.py sample_configs/interact.yaml`. 

Your setup is correct if, after running the command, you get something that looks like this. (Its expected that it will print other things before that too)

`Using <|endoftext|> as pad token
text (or STOP):`

If you then type `here is a test sentence`, this is what you should expect to see: 

```
word                 | Split | Unk | ModelName            | surp     | prob      
---------------------------------------------------------------------------------
here                 |     0 |   0 | gpt2                 |      0.0 |        1.0
 is                  |     0 |   0 | gpt2                 |    5.778 |    0.01822
 a                   |     0 |   0 | gpt2                 |    2.989 |    0.12592
 test                |     0 |   0 | gpt2                 |   10.786 |    0.00057
 sentence            |     0 |   0 | gpt2                 |   12.281 |     0.0002

```

And then if you type `STOP` it should exit the program. 


## Part 2: Installation on Turing

As we get to later parts in the class, you will likely want to run multiple models simultaneously, or run very large models, which can prove to be challenging on your personal computer. At that point, it would be helpful to use Colgate's HPC, Turing. 

To use Turing, you need to either be connected to eduroam on the Colgate campus or connect to the [VPN](https://www.colgate.edu/about/campus-services-and-resources/vpn-connections-campus-network).

1. Go to `turing.colgate.edu` and sign-in using your Colgate credentials. 
2. Click on `JupyterHub GPU`
3. Click on `Start My Server`
4. Open up a terminal window by clicking on the `+` button at the top left of the screen, and then picking terminal. 
5. Repeat steps 1-3 from Part 1, this time also following the Turing specific parts. 


## Part 3: Python refresher


The goal of this part is to serve as a Python refresher for: 

- File I/O
- Dictionaries
- Nested structures
- Doctests

You will also familiarize yourself with using Pandas and generating plots and in that process practice looking up how to do things that you are not quite sure about!

Concretely, for this part, you will build a toy text classification model. Note: this was the final homework for COSC 101 last semester. So while this could feel a little challenging (especially if you haven't worked with Python in a while), as students of a 400-level class, I am confident in your ability to complete this! 

### Background: Text classification 

Text classification is a common task in Natural Langauge Processing (NLP) that is used to assign a class label to some given text. Concretely, in this homework, you will train a model that will assign texts to one of two classes: Shakespeare or Swift. 

In order to classify texts, we need to compute some score for the model given each of the different classes, and then pick the class that has a higher score. Here is one approach we can use to calculate the score for a text given some class: 

1. Estimate the probability of each word in your vocabulary given the class using some training data. To calculate the probability of some word given a class, count the number of times the word occurs in the training data and divide it by the total number of words. In other words, use the following formula: 

 *P(word | class) = count(word, class train)/count(class train)*


2. Given some text you want to classify, compute the score by adding together the *log* probabilities of each of the words in the text given the class (as computed in step 1). *Note since we cannot take the log of 0 (just like we cannot divide by 0), we will always add some small value epsilon to the probability before taking the log.* 


### Example output

If your code is running correctly, then when you train your model on the training dataset, and evaluate it on the `swift_toy` and `shakespeare_toy` datasets in the `test` folder, then your code should generate a file that looks like `predictions_toy_gold.txt`. 

Apart from the final output, the starter code also has doctests that specify expected behavior for each of the intermediate steps. 


### Your tasks

#### Task A: Implement the helper functions

The starter file comes with `doctest`s for each function that explicitly specify input-output mappings for the function. In order to make it easier to implement the functions one at a time, all of the function definitions except the first function are commented out. Implement the first function, ensure that it passes all the doctests, before commenting out the next function. 

Each helper function should be very short. Feel free to add your own fruitful functions, each of which abstracting a process that you find repeated across the helper function you need to implement.

**Note: In writing some of the helper functions, you might have to compose previously written (and tested!) functions**

Implement the helper functions in the following order: 


- `clean_words`: Takes in a list of words and returns a new list with words in lowercase with the punctuation and other symbols removed. 

- `update_frequencies`: Updates the count dictionary (the one used to compte probabilities) with words in some file

- `get_probabilities`: Converts frequencies into probabilities

- `get_logprob_text`: Gets the summed log probability of all the words in a text given a probability dictionary

- `classify`: Given a text returns the class for the text that has the highest log probability. 

- `train`: For each class, trains a model (i.e., creates a probability dictionary) given a list of files. 

- `classify_texts`: Given trained models, and a list of files, classifies each of the lines in the files and writes all the predictions to an output file. 


**Hint: The `split()` function by default splits on *any* whitespace including spaces, new lines, tabs, etc**

#### Task B: Compose the helper functions

Once you have implemented, tested and debugged each these 7 functions, write the `main` function that implements the required functionality. Your main file should create two files: `predictions_toy.txt` which has the predictions for the toy test files, and `predictions.txt` which has the predictions for all the test files. **Note: Some parts of the main function are already created for you**

#### Task C: Evaluate model predictions

For this part, compute model accuracy in the `Lab0.ipynb` notebook. To open this notebook, navigate to the folder with the file in the command line, and then type `jupyter lab`. 


