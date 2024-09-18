import nltk
from nltk import CFG
from nltk import grammar
from nltk.parse.generate import generate
from nltk import ChartParser, word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')


def get_grammar(grammar_fname:str)->grammar.CFG:
    with open(grammar_fname) as f:
        grammar_str = f.read()

    return(CFG.fromstring(grammar_str))


def parse_sentence(sentence:str, grammar:grammar.CFG):
    chart_parser = ChartParser(grammar)
    tokens = word_tokenize(sentence)
    parses = chart_parser.parse(tokens)
    return list(parses) 

def generate_sentences(grammar: grammar.CFG, num_sents: int, max_depth=13) -> list:
    """
    Without max_depth a recursive grammar can cause run time error by hitting recursive stack depth limits.  
    """
    sents = generate(grammar, n=num_sents, depth=max_depth)

    return [' '.join(s) for s in sents]

def is_grammatical(sentence:str, grammar:grammar.CFG) -> bool:
    """
    Returns True if sentence is grammatical given the grammar, False otherwise
    """
    pass


def test_grammar2(grammar_fname: str):
    """
    Verifies that the grammar can only generate grammatical sentences. 
    """
    pass

def test_grammar3(grammar_fname: str):
    """
    Verifies that the grammar can only generate grammatical sentences. 
    """
    pass

def test_grammar4(grammar_fname: str):
    """
    Verifies that the grammar can only generate grammatical sentences. 
    """
    pass

def test_grammar5(grammar_fname: str):
    """
    Verifies that the grammar can only generate grammatical sentences. 
    """
    pass

def main():
    grammar = get_grammar('grammar1.txt')
    for sent in generate_sentences(grammar, num_sents=10):
        print(sent)

    sent = 'the panda saw my friend in her pajamas'

    for parse in parse_sentence(sent, grammar):
        parse.pretty_print() 

    sent2 = 'the pajamas ate my friend in the panda'

    for parse in parse_sentence(sent2, grammar):
        parse.pretty_print()


main()









