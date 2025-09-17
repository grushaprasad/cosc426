# COSC 426 F25 Lab 3

## Introduction
In this lab you will be writing grammars that can generate a subset of sentences that are grammatical in Standard American English (SAE), while ensuring that these grammars do not generate sentences that are ungrammatical. 

Through the course of six parts in this lab, you will incrementally create more complicated grammars. 

* Part 1: Familiarizing yourself with the grammar notation and reasoning about probability of sentences

* Part 2: Adding more verbs

* Part 3: Adding adjectives

* Part 4: Adding adverbs

* Part 5 (optional): Adding relative clauses 

* Part 6 (optional): Adding fronted sentential complements

**Please check-in with me after each part to make sure that you are on the right track**


### Grading
In order to get the `Meets Expectation` designation for this lab, you should correctly complete the first four parts. To get the `Exceeded Expectation` designation you should also correctly complete parts 5 or 6 (or both if you are curious!). 

### A note of ungrammaticality

Sometimes the sentences listed as "ungrammatical" might be grammatical in SAE. But for the purposes of this lab, you should treat these sentences as being ungrammatical for the langauge you are trying to model. 

## Provided files
- `Lab3.py`
- `Lab3.ipynb`
- `starter_grammar.txt`

## What to submit
- `Lab2.ipynb` with answers to all of the questions in all the parts, and any tests you run to check your grammars **Make sure that when you submit the file, the outputs in the cells are visible on gradescope.** 
- grammar1.txt for the grammar in Part 1
- grammar2.txt for the grammar in Part 2
- grammar3.txt for the grammar in Part 3
- grammar4.txt for the grammar in Part 4
- Optional: grammar5.txt and grammar6.txt for Parts 5 and 6 respectively

*Note: You do not have to change anything in `Lab3.py`.* 

**If you work in a group, one member of the group should create a submission on gradescope and add the others to the submission**


## Part 0
In this part familiarize yourself with the provided grammar in `starter_grammar.txt` and the starter code in `Lab3.ipynb`. Run the code in Part 0, and make sure you understand how to generate and parse sentences. 

## Part 1

Answer the following questions. 

1. What are the two interpretations of the sentence `a panda in a friend ate my pajamas in a sandwich`. 

2. What are some factors that influence the probability of a sentence? Explain. 

3. Create a copy of `starter_grammar.txt`and name it `grammar1.txt`. Modify `grammar1.txt` such that both the interpretations of `a panda in a friend ate my pajamas in a sandwich` have the same probability. **Note: by the end of this modification, you grammar should still produce the two parses.** 

4. Generate 25 sentences from this grammar. You will notice that this grammar sometimes generates very long sentences sometimes. Modify the grammar such that it generates fewer long sentences (but it is can still generate these long sentences). 

5. Complete the function `is_grammatical` in `Lab1.ipynb`. This function will be helpful as you test the grammars you write in the later parts.     


## Part 2 

Now improve the grammar from the previous step by adding in the following verbs: `existed`, `vanished`, `died`. 

### Data

**Your grammar should treat these sentences as grammatical**

- the panda existed 
- the panda ate
- the panda ate the sandwich
- the sandwich saw the panda in my friend
- the sandwich in my friend died in the panda
- my friend vanished in the sandwich
- my friend saw the sandwich in the panda in my friend

**Your grammar should treat these sentences as ungrammatical**

- the panda vanished my friend
- the sandwich existed the panda
- my friend in the sandwich died the panda
- the panda died the sandwich in my friend

### Your task

Answer the following questions:

1. Describe in one or two sentences, what is the pattern (or "generalization") that captures this (un)grammaticality? 
2. Write `grammar2.txt` that implements the generalization you described. 

## Part 3
Now improve the grammar from the previous step by adding in the following adjectives: `excited`, `delicious`, `ponderous`. 

### Data

**Your grammar should treat these sentences as grammatical**
- the ponderous panda existed
- the excited excited ponderous panda ate the sandwich
- the panda saw my very delicious delicious sandwich in my very very ponderous pajamas

**Your grammar should treat these sentences as ungrammatical**
- the panda ponderous existed
- the ponderous panda excited vanished
- the panda in the ponderous very pajamas saw my friend

### Your task

Answer the following questions:
1. Describe in one or two sentences, what is the pattern (or "generalization") that captures this (un)grammaticality? 
2. Write `grammar3.txt` that implements the generalization you described. 

## Part 4
Now improve the grammar from the previous step by adding in the following adverbs: `peacefully`, `joyfully`.  

### Data

**Your grammar should treat these sentences as grammatical**
- the panda vanished peacefully
- the ponderous pajamas peacefully died
- Peacefully the ponderous pajamas died
- the ponderous pajamas existed peacefully in my pajamas
- the panda peacefully saw the ponderous friend in my pajamas
- the panda saw the ponderous friend peacefully in my pajamas
- the panda saw the ponderous friend in my pajamas peacefully
- my very very ponderous friend existed very very very peacefully. 
- my friend ate the excited delicious sandwich peacefully joyfully in my pajamas

**Your grammar should treat these sentences as ungrammatical**
- the panda joyfully vanished peacefully
- my ponderous friend existed peacefully very very
- my friend very saw the sandwich in the pajamas
- my friend very saw peacefully the sandwich in the pajamas
- the joyfully pajamas saw the sandwich in the pajamas

### Your task

Answer the following questions:
1. Describe in one or two sentences, what is the pattern (or "generalization") that captures this (un)grammaticality? 
2. Write `grammar4.txt` that implements the generalization you described. 


## Part 5 (optional; for exceeds expectations)
Now improve the grammar from the previous step by adding in relative clauses that modify the subject of the clause.

### Data

**Your grammar should treat these sentences as grammatical**

- the panda that existed very peacefully vanished joyfully
- my friend saw the panda that existed very peacefully
- the panda that existed very joyfully died peacefully
- the panda saw my friend that joyfully ate the sanwich in her pajamas 
- the panda saw my very excited friend in her pajamas that joyfully peacefully existed 


**Your grammar should treat these sentences as ungrammatical**

- the panda that existed my friend ate the sandwich
- the sandwich saw that my friend existed (note this is grammatical in English but a different construction)
- the panda that vanished peacefully in my friend
- the panda existed very joyfully died peacefully

### Your task

Answer the following questions:
1. Describe in one or two sentences, what is the pattern (or "generalization") that captures this (un)grammaticality? 
2. Write `grammar5.txt` that implements the generalization you described. 

## Part 6 (optional; for exceeds expectations)
Finally improve the grammar from the previous step by adding an even more complex structure: fronted sentential complements.

### Data

**Your grammar should treat these sentences as grammatical**

- that my friend ate the excited delicious sandwich peacefully joyfully in my pajamas pleased the panda

- that the excited panda vanished peacefully perplexed my friend

- that my friend in the pajamas saw the very very very excited panda surprised the sandwich

- that the panda that existed very peacefully vanished joyfully perplexed my friend 

- that the panda that existed very peacefully vanished joyfully perplexed my friend that ate the sandwich

**Your grammar should treat these sentences as ungrammatical**

- that my friend pleased the panda ate the excited delicious sandwich  

- that the excited panda vanished peacefully perplexed 

- my friend in the pajamas saw the very very very excited panda surprised the sandwich

- that the panda existed very peacefully vanished joyfully surprised my friend that 

### Your task

Answer the following questions:

1. Describe in one or two sentences, what is the pattern (or "generalization") that captures this (un)grammaticality? 
2. Write `grammar6.txt` that implements the generalization you described. 


