import numpy as np
import nltk
import re
import random
import math
nltk.download('punkt')

def create_pcfg(fname:str):
    with open(fname, 'r') as f:
        rules = f.readlines()

    rules = [rule for rule in rules if len(rule.strip()) > 0 and rule[0] != '#'] # remove empty lines and comments

    pcfg = {}
    for rule in rules:
        lhs, rhs =  rule.split('->')
        lhs = lhs.strip()
        curr_rules = rhs.split('|') # in case there are multiple
        for curr_rule in curr_rules:
            weight = re.findall(r'\[.*\]', curr_rule)[0]
            weight = float(weight.replace('[', '').replace(']', ''))
            curr_rhs = re.sub(r'\[.*\]', '', curr_rule).strip()
            pcfg[lhs] = pcfg.get(lhs, []) + [(curr_rhs, weight)]

    return pcfg


def pick_random(list_of_tuples):
    rules = [x[0] for x in list_of_tuples]
    probs = [x[1] for x in list_of_tuples]
    choice = random.choices(population=list_of_tuples, 
                            weights = probs,
                            k= 1)
    return list(choice)[0]

    # return list(np.random.choice(rules, 1, probs))

def generate(rule, logprob, sentence, grammar):
    sub_rules = rule.split()

    if len(sub_rules) == 1 and sub_rules[0] not in grammar: #reached terminal
        sentence.append(rule)
    else:
        for curr_rule in sub_rules:
            next_rule, next_prob = pick_random(grammar[curr_rule])

            logprob.append(math.log2(next_prob))
            generate(next_rule, logprob, sentence, grammar)

    sentence = [x.replace("'", "") for x in sentence]
    return(' '.join(sentence), np.sum(logprob))





def generate_sentences(grammar: dict, num_sents: int) -> list:
    """
    Generates num_sents, sampled probabilistically from grammar
    """

    sents = []

    for i in range(num_sents):
        sents.append(generate('ROOT', [], [], grammar))
    return sents

def parse_sentence(grammar_fname: str, sentence: str):
    with open(grammar_fname, 'r') as f:
        grammar = nltk.PCFG.fromstring(f.read())

    parser = nltk.parse.InsideChartParser(grammar)

    return parser.parse(sentence.split())

    # for tree in parser.parse(sentence.split()):
    #     tree.pretty_print()



if __name__ == '__main__':
    grammar = create_pcfg('grammar1.txt')
    sents = generate_sentences(grammar, 10)

    for sent in sents:
        print(sent,'\n')

    # chart_parser = nltk.ChartParser(nltk.PCFG.fromstring(grammar))

    # for sent in sentences:
    #   print(sent)
    #   tokens = nltk.word_tokenize(sent)
    #   for tree in chart_parser.parse(tokens):
    #      tree.pretty_print()







