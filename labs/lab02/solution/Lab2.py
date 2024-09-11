def load_verbs(fname: str) -> dict:

    verbs = {}
    with open(fname, 'r') as f:
        f.readline()
        for line in f:
            line = line.strip().split()
            if line[0] not in verbs:
                verbs[line[0]] = []
            verbs[line[0]].append(line[1])
    return verbs 

def load_nouns(fname: str) -> dict:

    nouns = {}
    with open(fname, 'r') as f:
        f.readline()
        for line in f:
            line = line.strip().split()
            if line[0] not in nouns:
                nouns[line[0]] = []
            nouns[line[0]].append(line[1])
    return nouns

def create_stim(verbs:dict, nouns:dict, 
                outname: str) -> None:

    file = open(outname, 'w')
    header = ['sentid', 'comparison', 'pairid', 'contextid', 'lemma',
              'condition', 'pronoun', 'sentence', 'ROI']
    file.write('\t'.join(header)+'\n')
    sentid = 0
    ROI = '4,5'
    contextid = 0
    for verb in verbs['subject']: 
        condition = 'subject'
        lemma = verb
        pairid = 0
        for male in nouns['male']:
            for female in nouns['female']: 
                mf_he = ' '.join([male, verb, female, 'because', 'he'])
                mf_she = ' '.join([male, verb, female, 'because', 'she'])

                fm_he = ' '.join([female, verb, male, 'because', 'he'])
                fm_she = ' '.join([female, verb, male, 'because', 'she'])

                sentences = [mf_he, mf_she, fm_he, fm_she]

                comparisons = ['expected', 'unexpected', 'unexpected',
                               'expected']
                pronouns = ['he', 'she', 'he', 'she']

                for idx, (sentence, comparison, pronoun) in enumerate(zip(sentences, comparisons,
                                                         pronouns,
                                                                          strict=True)):

                    entry = [sentid, comparison, pairid, contextid, lemma,
                             condition, pronoun, sentence, ROI]
                    entry = list(map(lambda x: str(x), entry))
                    file.write('\t'.join(entry)+'\n')
                    if idx%2 == 1:
                        pairid += 1
                    sentid += 1
        contextid += 1

    for verb in verbs['object']: 
        condition = 'object'
        lemma = verb
        pairid = 0
        for male in nouns['male']:
            for female in nouns['female']: 
                mf_he = ' '.join([male, verb, female, 'because', 'he'])
                mf_she = ' '.join([male, verb, female, 'because', 'she'])

                fm_he = ' '.join([female, verb, male, 'because', 'he'])
                fm_she = ' '.join([female, verb, male, 'because', 'she'])

                sentences = [mf_he, mf_she, fm_he, fm_she]

                comparisons = ['unexpected', 'expected', 'expected',
                               'unexpected']
                pronouns = ['he', 'she', 'he', 'she']

                for idx, (sentence, comparison, pronoun) in enumerate(zip(sentences, comparisons,
                                                         pronouns,
                                                                          strict=True)):

                    entry = [sentid, comparison, pairid, contextid, lemma,
                             condition, pronoun, sentence, ROI]
                    entry = list(map(lambda x: str(x), entry))
                    file.write('\t'.join(entry)+'\n')
                    if idx%2 == 1:
                        pairid += 1
                    sentid += 1
        contextid += 1

    file.close()


def plot(resultsfname: str,
         xname: str, yname: str, outname: str) -> None:
    import seaborn as sns
    import pandas as pd
    data = pd.read_csv(resultsfname, sep='\t')

    # Plot the orbital period with horizontal boxes
    g = sns.barplot(data=data, x=xname, y=yname)
    g.figure.savefig(outname)


if __name__ == "__main__":
    verbs = 'IC.tsv'
    nouns = 'nouns.tsv'

    verbs = load_verbs(verbs)
    nouns = load_nouns(nouns)
    create_stim(verbs, nouns, 'stim.tsv')

    plot('sample_data.tsv', 'condition', 'microdiff', 'plot.png')

