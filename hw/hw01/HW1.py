import nltk
from nltk import CFG
from nltk import grammar
from nltk.parse.generate import generate
from nltk import ChartParser, word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')

import random



def get_grammar(grammar_fname:str)->grammar.CFG:
    with open(grammar_fname) as f:
        grammar_str = f.read()

    return(CFG.fromstring(grammar_str))


def parse_sentence(sentence:str, grammar:grammar.CFG) -> list:
    chart_parser = ChartParser(grammar)
    tokens = word_tokenize(sentence)
    parses = chart_parser.parse(tokens)
    return list(parses) 

def generate_sentences(grammar: grammar.CFG, num_sents: int, max_depth=13) -> list:
    ## generates all possible sentences of a certain depth
    sents = generate(grammar, depth=max_depth)

    sents = list(sents)
    print(len(sents))
    random.shuffle(sents)
    sents = sents[:num_sents]

    return [' '.join(s) for s in sents]

def is_grammatical(sentence:str, grammar:grammar.CFG) -> bool:
    """

    """
    parses = parse_sentence(sentence, grammar)
    return len(parses) > 0


def create_train_val(sents: list, train_fname:str, val_fname: str, split_prop: int):
    n = len(sents)*split_prop
    train_sents = sents[:n]
    val_sents = sents[n:]
    with open(train_fname, 'w') as f:
        f.write('text\n') #needs to have column called text

        for sent in train_sents:
            f.write(sent + '\n')

    with open(val_fname, 'w') as f:
        f.write('text\n') #needs to have column called text
        for sent in val_sents:
            f.write(sent + '\n')


def main():
    ## Test your grammar

    ## Create training and validation data
    
    pass

main()









