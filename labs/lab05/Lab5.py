import nltk
import math

def getVocab(vocab_fname: str) -> set: 
    """
    Args: 
        vocab_fname: filepath to vocab file. Each line has a new vocab item

    Returns: 
        A set of all the vocabulary items in the file plus three additional tokens: 
            - [UNK] : to represent words in the text not in the vocab
            - [BOS] : to represent the beginning of sentences. 
            - [EOS] : to represent the end of sentences. 
        If you run this function on the glove vocab, it should return set with 400003 items.
    """

    with open(vocab_fname, 'r') as f:
        dat = f.read().split('\n')

    pass

def preprocess(text:str, mark_ends: bool) -> list:
    """
    Args: 
        text: some text

        mark_ends: indicates whether sentences should start with [BOS] and end with [EOS]

    Returns: 
        A list of lists where each sublist consists of tokens from each sentence. 
        Use existing nltk functions to first divide the text into sentences, and then into words. 

        If you run preprocess on the text in test.txt with mark_ends=True you should get the following list: 
            [['[BOS]', 'one', 'thing', 'was', 'certain', ',', 'that', 'the', '_white_', 'kitten', 'had', 'had', 'nothing', 'to', 'do', 'with', 'it', ':', '—it', 'was', 'the', 'black', 'kitten', '’', 's', 'fault', 'entirely', '.', '[EOS]'], ['[BOS]', 'for', 'the', 'white', 'kitten', 'had', 'been', 'having', 'its', 'face', 'washed', 'by', 'the', 'old', 'cat', 'for', 'the', 'last', 'quarter', 'of', 'an', 'hour', '(', 'and', 'bearing', 'it', 'pretty', 'well', ',', 'considering', ')', ';', 'so', 'you', 'see', 'that', 'it', '_couldn', '’', 't_', 'have', 'had', 'any', 'hand', 'in', 'the', 'mischief', '.', '[EOS]']]
    """
    pass



def getBigramFreqs(preprocessed_text:list, vocab:set) -> dict:
    """
    Args: 
        preprocessed_text: text that has been divided into sentences and tokens


    Returns: 
        dictionary with all bigrams that occur in the text along with frequencies. 
        Each key should be a tuple of strings of the format (first_token, second_token). 

        If you run this function on the text from above with mark_ends as True, it should return: 
            73 bigrams
            The following 3 bigrams should have count 2: ([BOS], UNK), (kitten, had) and (. , [EOS])
            All other bigrams should have count of 1. 
    """
    pass

def getBigramProb(bigram: tuple, smooth: str, **kwargs):
    """
    Args:
        bigram: the tuple of the bigram you want the prob of
        smooth: MLE (no smoothing), add-k where you add k to all bigram counts.  
        **kwargs: other parameters you might want. 

        Hint: think about what parameters do you want to pass in so you minimize redundant computation. 

    Returns:
        float with prob. 
        Return -1.0 if invalid smoothing value is entered. 

        Here are the probabilities for some bigrams from test.txt
        
        MLE: 
            ('one', 'thing') 1.0
            ('kitten', 'had') 0.6666666666666666
            ('cat', 'had') 0.0
            ('had', 'had') 0.25
            ('on', 'the') 0.0
            ('held', 'a') 0.0
            ('zzzzzzz', 'the') 0.0

        add-0.1:
            ('one', 'thing') 2.749910627904593e-05
            ('kitten', 'had') 5.2495669107298645e-05
            ('cat', 'had') 2.4999187526405393e-06
            ('had', 'had') 2.7497044067762715e-05
            ('on', 'the') 2.4999812501406237e-06
            ('held', 'a') 2.4999812501406237e-06
            ('zzzzzzz', 'the') 2.4997312788875196e-06

    """
    pass


def calcPerplexity(text: str, mark_ends: bool, smooth: str, **kwargs) -> float:
    """
    Args:
        text: text to calculate perplexity of 
        mark_ends: indicates whether sentences should start with [BOS] and end with [EOS]
        smooth: MLE (no smoothing), add-k where you add k to all bigram counts
        **kwargs: other parameters you might want. 

    Returns: 
        Bigram perplexity of the text given a trained bigram language model. 
        perplexity = - 2^(- (1/N) sum_x log2(x)) where x iterates through each bigram in the text and N=number of bigrams 

        Hint: think about what parameters you need in order to specify a trained bigram langauge model. 

        Here is the perplexity for four sentences when using a bigram model trained on test.txt with add-0.1 smoothing and mark_ends set to True

        it was the black kitten’s fault entirely 74664.17211996247
        it was not the black cat’s fault really 208001.1874970506
        here is a random sentence 400006.33326389204
        here is a random sentence matched for length 400007.44435802946

        And the perplexity of the entire test.txt is 34555.90939877085
    
    """
    pass


def main():
    """
    Call your functions and write your test cases here

    """

    pass
