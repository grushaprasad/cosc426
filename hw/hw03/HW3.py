from webbrowser import get
import nltk
from transformers import AutoTokenizer
import math
import pandas as pd

def get_vocab(vocab_fname: str) -> set:
    """
    Args:
        vocab_fname: filepath to vocab file. Each line has a new vocab item

    Returns:
        A set of all the vocabulary items in the file plus three additional tokens:
            - [UNK] : to represent words in the text not in the vocab
            - [BOS] : to represent the beginning of sentences.
            - [EOS] : to represent the end of sentences.
        If you run this function on the glove vocab, it should return set with 400003 items.

    >>> len(getVocab('glove_vocab.txt'))
    400003
    """

    with open(vocab_fname, "r") as f:
        dat = f.read().split("\n")

    dat = set([item.strip() for item in dat if len(item) > 0])
    dat.add("[UNK]")
    dat.add("[BOS]")
    dat.add("[EOS]")
    return dat


def get_ngrams(text: list, n):
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


def preprocess(textfname: str, lower: bool, tokenizer, **kwargs):
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
    modelname = kwargs["modelname"]

    tokenizer = AutoTokenizer.from_pretrained(modelname)
    tokenized_output = tokenizer(text)
    words = tokenizer.convert_ids_to_tokens(tokenized_output["input_ids"])
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
    vocab = get_vocab("data/glove_vocab.txt")
    text = preprocess("data/test.txt", True, hf_tokenize, modelname="distilgpt2")
    print(text)
    bigram_freqs = get_ngramFreqs(text, 2)
    bigrams = get_ngrams(text, 2)

    print(get_ngramProbs(text, 2, vocab, "add-1"))
    print(get_ngramProbs(text, 1, vocab))

    for bigram in bigrams:
        if bigram_freqs[bigram] != 1:
            print(bigram, bigram_freqs[bigram])

    print(len(get_hf_vocab("distilgpt2")))


def get_ngramProbs(text: list, n: int, vocab: set, smooth: str = "MLE"):
    """Get the probabilities of ngrams

    Returns:
        probs: dictionary of ngram probabilities
    """
    k = 0.0
    v = len(vocab)
    total_words = len(text)  # for unigram
    freqs = {}
    target_freqs = {}
    probs = {}

    if smooth.startswith("add-"):
        k = float(smooth.split("-")[1])
        if k < 0:
            raise ValueError("k must be non-negative")

    print(f"Using smoothing with k={k}")

    for i in range(1, n + 1):  # get all ngram freqs up to n
        ngram_freqs = get_ngramFreqs(text, i)
        freqs = freqs | ngram_freqs
        if i == n:
            target_freqs = ngram_freqs

    if n == 1:  # unigram
        for unigram, freq in target_freqs.items():
            probs[unigram] = (freq + k) / (total_words + k * v)
        return probs

    for ngram, freq in target_freqs.items():  # ngram
        pfreq = freqs[ngram[: n - 1]]  # context frequency
        probs[ngram] = (freq + k) / (pfreq + k * v)
    return probs


def evaluate(text: list, n: int, smooth: str, vocab: list):
    total = 0
    count = 0
    probs = get_ngramProbs(text, n, vocab, smooth)
    for i in range(len(text) - n + 1):
        total += probs[text[i : i + n]]
        count += 1

    return total / count


if __name__ == "__main__":
    tests()
