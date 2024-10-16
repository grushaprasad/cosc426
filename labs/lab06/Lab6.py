from BigramModel import BigramModel
import nltk
import random
random.seed(17)
import pandas as pd
import math
import numpy as np


def usingBigramClass():
    """
    Demonstration of how to use BigramModel class
    
    """

    test_model = BigramModel(tokenizer = nltk.word_tokenize,
                         vocab_fname = '../glove_vocab.txt',
                         train_fpath = '../sample_data/sample_train.txt',
                         mark_ends = True,
                         smooth='add-0.1')

    print(test_model.getBigramProb(bigram = ('kitten', 'had'))) # 5.2495669107298645e-05


    test_model.evaluate(eval_fpath='../sample_data/sample_test.txt',
                        result_fpath='../sample_data/sample_preds.tsv')



## Write your code for classification here

def write_file(fname, lst):
    with open(fname, 'w') as f:
        for line in lst:
            f.write(f'{line.strip()}\n')

def summarize(fname:str, aggregrate_type:str, aggregrate_col:str, groupby_cols:list, delimiter='\t'):
    """
    Args:
        fname: fpath to tsv/ csv file
        aggregate_type: mean or sum

        aggrefate_col: the column with values you want to aggregate over

        groupby_cols: the columns with the groups. 

    Returns:
        Pandas Dataframe with as many rows as unique group combinations. The values of rows in each group is either summed together or averaged depending on the aggregate_type. 

    """
    dat = pd.read_csv(fname, sep=delimiter)

    summ = dat.groupby(groupby_cols).agg({aggregrate_col: aggregrate_type}).reset_index()

    return summ



def split_class(fname:str, delimiter:str, header=False):
    """
    Args:
        dat: Name of file with data. Each line in the file has two elements: text (e.g., review), label (e.g., positive)

        delimiter: the delimiter that separates text and label
        header: if True, first line is column names and should be ignored

    Output: 
        Creates a file for each class in the dataset. If you run the function on sample_reviews.txt, it should create the following files:
        1. sample_reviews_positive.txt
        2. sample_reviews_negative.txt

    """
    pass


def get_prior(data: dict) -> dict:
    """
    Args:
        data: dictionary where keys are the classes, and values are filepaths to the class specific data

    Returns:
        Dictionary with prior probability for each class, which is the number of lines of text in the class divided by the total number of lines of text across all classes. 

    If you input 
    prior_dict = {'positive': 'sample_reviews_positive.txt',
                  'negative': 'sample_reviews_negative.txt'}

    You should get {'positive': 0.6, 'negative': 0.4}

    """
    pass


def get_likelihood(models_dict, eval_fpath, class_label):
    """
    Args:
        Dictionary where keys are classes and values are the models trained on the classes

        eval_fpath: the file models should be evaluated on. 

    Returns:
        A Dataframe with the following columns: sentid, model, likelihood, class. Likelihood of a sequence is the sum of log probability across all the words in the sequence.

    If you set eval_fpath to sample_reviews_test_positive.txt, you should get a dataframe that looks like this. (Its ok if you end up havind additional columns)

        sentid  model       likelihood     class
    0       0   positive    -100.975898  positive
    1       1   positive    -100.941133  positive
    0       0   negative    -101.938780  positive
    1       1   negative    -101.938780  positive

    Hint: think about if any of the helper functions provided are useful here. 

    """

    pass
    

def get_posterior(models_dict, eval_fpath, class_label, prior_dict):
    """
    Args:
        Dictionary where keys are classes and values are the models trained on the classes

        eval_fpath: the file models should be evaluated on. 

        class_label: the label of the file that models are evaluated on

        prior_dict: prior probabilities of classes

    Returns:
        A Dataframe with the following columns: sentid, model, likelihood, class. 

    If you set eval_fpath to sample_reviews_test_positive.txt, you should get a dataframe that looks like this. (Its ok if you end up having additional columns)

   sentid model     likelihood   class        prior      posterior
       0  positive  -100.975898  positive    -0.736966   -101.712864
       1  positive  -100.941133  positive    -0.736966   -101.678099
       0  negative  -101.938780  positive    -1.321928   -103.260708
       1  negative  -101.938780  positive    -1.321928   -103.260708


    """

    pass


def classify(posterior):
    """
    Args:
        Dataframe with posterior probabilities

    Returns: 
        Dataframe where each sentence id is associated with a prediction. 

    If you compute posterior from sample_reviews_test_positive.txt, you should get a dataframe that looks like this (its ok if you have extra columns)

    sentid    negative      positive        pred
    0       -103.260708     -101.712864     positive
    1       -103.260708     -101.678099     positive

    """

    # converts the data from long to wide
    wide_df = posterior.pivot(index=['sentid'], columns=['model'], values='posterior').reset_index()

    #Finish the rest of the function 
    pass


def calc_accuracy(models_dict, eval_dict, prior_dict):
    """
    Args:
        models_dict: keys are classes, values are models trained on data from the class. 

        eval_dict: keys are classes, values are fpaths to evaluation data where the correct label is the class associated with the key

        prior_dict: keys are classes, values are prior probabilties of the classes. 

    Returns:
        Float which is the accuracy of the predictions across all classes

    """

    pass






def main():
    """
    Print accuracy of a add-0.0001 bigram model trained on sample_reviews.txt when evaluated on sample_reviews_test.txt. 

    """
    pass


uisngBigram()
main()


