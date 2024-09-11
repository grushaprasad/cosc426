def get_freqs(fname: str, start: int, end: int) -> dict:
    """
    Args:
        fname (str): A variable holding the name of file to read 
        start (int): the line in file from which to start looking for words
        end (int): the line in file from which to end looking for words. 

        Start and end can be useful if you want to ignore things like license.

    Returns:
        A dict mapping words (i.e. space delinated tokens by line) to its
        frequency in a corpus. For example,

        With a file containing:
            The cat ate the cat food.
            Well, the cat loves food!

        This should return:

            {'the': 3, 'cat': 3, 'ate': 1, 'food.': 1, 'food!': 1, 'well,': 1, 'loves': 1}

    Hints:
        Make sure to remove new line characters.
        Notice the presence/absence of capitalization and punctuation. 

        For a nice introduction to python dictionaries see https://realpython.com/python-dicts/

    """

    pass

def getWord(freqs: dict, n: int) -> str:
    """
    Args:
        freqs (dict): Frequencies of all the words
        n (int): Which word in the dictionary to return. 

    Returns: 
        A string. If n is positive, then it returns the nth most frequent string. If n is negative it returns the nth least frequent string. Return an empty string if n is out of bounds.  
    """

    pass

def getSents(fname: str, word: str, n: int, start:int, end:int) -> list:
    """
    Args: 
        fname (str): A variable holding the name of file to read
        word (str): A word in the file
        n (int): 
        start (int): the line in file from which to start looking for words
        end (int): the line in file from which to end looking for words. 

        Start and end can be useful if you want to ignore things like license.

    Returns:
        A list of n sentences from the file which have the word. You can assume for now that sentences are separated by linebreaks (although this is a very inaccurate assumption to make) 
    """

    pass