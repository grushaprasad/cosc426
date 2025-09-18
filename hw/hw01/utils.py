import pandas as pd


def read_data(fpath, sheet_name=0, skiprows=None):
    """Read data from an Excel file and return as a pandas DataFrame."""
    import pandas as pd
    return pd.read_excel(fpath, sheet_name=sheet_name, skiprows=skiprows)

def generate_sentence(verb, np1, np2, pronoun):
    return f"{np1} {verb} {np2} becuase {pronoun} ..."

def generate_dataset(df: pd.DataFrame, np1 = "Mary", np2= "John"):
    pronouns = ["she", "he"] # she -> NP1, he -> NP2
    rows = []
    idx = 1
    median_frequency = df['Word Frequency (CELEX)'].median()
    for pair_id, df_row in df.iterrows():
        for pronoun in pronouns:
            if df_row['NP1'] == df_row['NP2'] or df_row["Word Frequency (CELEX)"] == median_frequency:
                continue # skip neutral verbs
            bias = "NP1" if df_row['NP1'] > df_row['NP2'] else "NP2"
            comparison = 'expected' if (bias == "NP1" and pronoun == "she") or (bias == "NP2" and pronoun == "he") else 'unexpected'
            frequency = 'frequent' if df_row["Word Frequency (CELEX)"] > median_frequency else 'infrequent'
            sentence = generate_sentence(df_row['Verb'], np1, np2, pronoun)
            
            new_row = { "sentid": idx,
                        "pairid": pair_id + 1,
                        "comparison": comparison,
                        "sentence": sentence,
                        "ROI": 4,
                        "bias": bias,
                        "frequency": frequency
                      }
            rows.append(new_row)
            idx += 1
    result = pd.DataFrame(rows)

    return result