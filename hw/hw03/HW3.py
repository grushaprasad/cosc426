import nltk
from transformers import AutoTokenizer

def get_ngrams(text:list, n):
    """
    Params:
        text: tokenized text in a list
        n: the n of the ngram

    Returns:
        list of all ngrams
    """
    return list(nltk.ngrams(text, n))

def get_ngramFreqs(text: list, n: int):
    """
    Params:
        text: text, split into list of tokens 
        n: the n for ngram

    Returns:
        Frequnency dictionary
    """

    ngrams = get_ngrams(text, n)
    freq_dict = nltk.probability.FreqDist(ngrams)

    return freq_dict

def preprocess(textfname: list, lower, tokenizer, **kwargs):
    """
    Params:
        textfname: path to text file. 
        tokenizer: tokenizing function 
        **kwargs: other kwargs for the tokenizer

    Returns: 
        List of tokens in the text

    """
    tokens = []
    print(f'Reading {textfname}')
    with open(textfname, 'r') as f:
        text = f.readlines()

    for i,line in enumerate(text):
        if lower:
            line = line.lower()
        tokens.extend(tokenizer(line, kwargs))
        if i%100 == 0:
            print(f'Tokenized {i+1} lines')

    return tokens

def hf_tokenize(text:str, kwargs):
    """
    Params: 
        text: string of text
        kwargs: dictionary with kwargs. Should include key 'modelname' which specifies the hf modelname
    Returns: 


    """
    modelname = kwargs['modelname']

    tokenizer = AutoTokenizer.from_pretrained(modelname)
    tokenized_output = tokenizer(text)
    words = tokenizer.convert_ids_to_tokens(tokenized_output['input_ids'])
    return words

def get_hf_vocab(modelname):
    """
    Params:
        modelname: string of hf modelname
    Returns:
        The vocabulary used by the huggingface model 

    """
    tokenizer = AutoTokenizer.from_pretrained(modelname)
    return tokenizer.vocab


def tests():
    
    text = preprocess('data/test.txt', True, hf_tokenize, modelname='distilgpt2')

    bigram_freqs = get_ngramFreqs(text, 2)

    bigrams = get_ngrams(text, 2)

    for bigram in bigrams:
        if bigram_freqs[bigram] !=1:
            print(bigram, bigram_freqs[bigram])

    print(len(get_hf_vocab('distilgpt2')))

if __name__ == "__main__":
    tests()