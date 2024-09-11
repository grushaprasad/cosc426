
def plot(resultsfname: str,
         xname: str, yname: str, outname: str) -> None:
    import seaborn as sns
    import pandas as pd
    data = pd.read_csv(resultsfname, sep='\t')

    # Plot the orbital period with horizontal boxes
    g = sns.barplot(data=data, x=xname, y=yname)
    g.figure.savefig(outname)


if __name__ == "__main__":

    plot('sample_data.tsv', 'condition', 'microdiff', 'plot.png')

