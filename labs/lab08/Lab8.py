import pandas as pd

def cleanPredFile(predfname: str) -> pd.DataFrame: 
    """ Cleans up predictions by dropping subwords and entries with no
    prediction.

    Parameters: 
        predfname (str): Name of the prediction file (the predfpath created in
                        `evaluate` mode)
    Returns:
        pd.DataFrame: Cleaned data frame of predictions 
    """
    predictions = pd.read_csv(predfname, sep='\t')
    # Drop subwords 
    predictions =  predictions[~predictions['token'].astype(str).str.contains('##')]
    # Drop nan predictions/words
    predictions = predictions[predictions['predicted'].notna()]
    predictions = predictions[predictions['word'].notna()]
    return predictions


def format_evaluate_data(fname: str) -> pd.DataFrame: 
    """ Format the ner data for `evaluate` mode with `NLPScholar`

    Parameters:
        fname (str): The name of jsonl file
    Returns:
        pd.DataFrame: The data in a dataframe with the correct format for
                    NLPScholar

    For example, 
    formate_evaluate('ner_news_data/english_news_weak_ner_small_test.jsonl')
    should yield a dataframe whose first 5 lines look like: 

       textid                                               text condition                                             target
    0       0  Source : Statistics New Zealand To contact the...      test  O O B-ORG I-ORG L-ORG O O O O O O O O B-PER L-...
    1       1                                           Abrams .      test                                            U-PER O
    2       2  Governor Perng Fai - nan and his board increas...      test  U-PER B-PER I-PER I-PER L-PER O O O O O O O O ...
    3       3  To contact the reporter on this story : David ...      test  O O O O O O O O B-PER L-PER O B-LOC L-LOC O U-...
    4       4  “ We need to invest more in the Americas , whi...      test                  O O O O O O O O U-LOC O O O O O O

    See ner_news_data/sample_ner_evalute_mode_data.tsv for the above output as a
    file.

    """

    raise NotImplementedError

    

def extractEntities(predfname: str) -> list: 
    """ Extract entities from the output of `evaluate` mode with `NLPScholar`.
    Only extract person, location, and organization entities.

    Parameters: 
        predfname (str): Name of the prediction file (the predfpath created in
                        `evaluate` mode)

    Returns:
        list[dict]: Per-textid entities where each text is given a dictionary
                with textid and entities as keys. 

    For example assuming you have a predictions file called preds.tsv you would
    see something like the following for the first three elements in the
    returned list:  

        [
        {'textid': 0, 
              'entities': [['Statistics New Zealand', 'ORG'], 
                            ['Daniel Petrie', 'PER'], ['Sydney', 'LOC'], 
                            ['Marco Babic', 'PER']]}, 
        {'textid': 1, 
             'entities': [['Abrams', 'PER']]}, 
        {'textid': 2, 
             'entities': [['Governor Perng Fai -', 'PER'], ['Bloomberg News', 'ORG']]}
        ]

    """

    predictions = cleanPredFile(predfname)

    raise NotImplementedError

if __name__ == "__main__":

    # Create evaluation data
    # Train Model
    # Run Evaluate with NLPScholar
    # Then extract entities
    pass
