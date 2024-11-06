import pandas as pd
import random

def create_database(datafpath: str, predfname: str) -> dict:
    """ Create a ner tagged database of news

    Parameters:
        datafpath (str): Filename of data from the evaluate config
        predfname (str): NER evaluate output for the data
    Returns: 
        dict: a dictionary mapping entity labels (e.g., PER) to phrases and text 

    It should look something like this
    {'PER':
        {'Lt Ivan Molchanets': ['Lt. Ivan Molchanets peeked over a parapet of sand
        bags at the front line of the war in Ukraine. Next to him was an empty
        helmet propped up to trick snipers, already perforated with multiple
        holes.', ... ],
        'Trent Williams': ['Team officials in Washington "emphatically" denied a
        rumor of a Trent Williams trade to Cleveland, according to a report
        Tuesday. A day later, Browns General Manager John Dorsey admitted
        publicly he has talked to Washington president Bruce Allen. "We\'ve had
        a few conversations," Dorsey said, via Mary Kay Cabot of the Cleveland
        Plain Dealer. "It [more]', ...]
        ...},
    'LOC':
        {'Ukraine': ['Lt. Ivan Molchanets peeked over a parapet of sand bags at
        the front line of the war in Ukraine. Next to him was an empty helmet
        propped up to trick snipers, already perforated with multiple holes.',
        ... ], 
        'Orlando': ["There won't be a chill down to your bones this Halloween in
        Orlando, unless you count the sweat dripping from your armpits.", ...]
        'Chile': ['Three people have died in a supermarket fire as angry protests
         in Chile entered their seventh day, the mayor of capital city Santiago
         said on Sunday.', ... ]
         ...},
    'ORG':
        {'NBA': ["I felt like I was a fraud, and being an NBA wife didn't help
        that. In fact, it nearly destroyed me.", ...]
        'Reader ' s Digest': ["They seem harmless, but there's a very good
        reason you shouldn't ignore them. The post How to Get Rid of Skin Tags,
        According to a Dermatologist appeared first on Reader's Digest.", ...]
        'NFL': ["Several fines came down against NFL players for criticizing
        officiating this week. It's a very bad look for the league."]
        ...}
    }
    """
    raise NotImplementedError


def search(database: dict, k:int = 5) -> None:
    """ Set up a search 'interface' 

    Parameters:
        database (dict): A database as returned from create_database
        k (int): The number of articles to display for the query

    Returns:
        None

    This should function as a interface where users provide a entity tag and a
    phrase and k articles are displayed. Here are some examples: 

        Entity tag (PER|LOC|ORG|STOP): DATE
        Tag not in database
        Entity tag (PER|LOC|ORG|STOP): LOC
        Search phrase: Syracuse
                 Four years ago, a jury convicted Robert Neulander, a prominent
                 doctor in central New York, of killing his wife in their
                 suburban home, seemingly ending a complicated case that had
                 riveted the Syracuse area. It was actually about to get more
                 complicated. On the day of the verdict, an alternate juror
                 contacted a lawyer for Mr. Neulander.

                 While this system didn't break any snow records in Syracuse, it brought
                 plenty of cold. Record low maximum for Nov. 12 was shattered by five
                 degrees, the new record of 27 was set on Tuesday and a new record low
                 was also set in Syracuse for this date as the mercury dipped to the
                 lower teens.

                 Four years ago, a jury convicted Robert Neulander, a prominent
                 doctor in central New York, of killing his wife in their
                 suburban home, seemingly ending a complicated case that had
                 riveted the Syracuse area. It was actually about to get more
                 complicated. On the day of the verdict, an alternate juror
                 contacted a lawyer for Mr. Neulander.

                 Spencer Martin re-assigned to Syracuse and two forwards sent to
                 Orlando.

        Entity tag (PER|LOC|ORG|STOP): ORG
        Search phrase: Colgate University
        Phrase not found

    """
    raise NotImplementedError

if __name__ == '__main__':

    # Create database
    # Search it
    pass

