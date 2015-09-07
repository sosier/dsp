"""
PROMPT:
# !/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program
should be called from the command line with two arguments: the name of a file
containing text to read, and the number of words to generate. For example, if
`chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself
playing our well-connected game went on. Our friend was absolutely correct:
nobody from the group needed this way. We never been as the Earth has the
network of eternity.

# There are design choices to make; feel free to experiment and shape the
program as you see fit. Jeff Atwood's
[Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place
to get started learning about what you're trying to make.

NOTE:

This module is based on of the markov code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html


UPDATES:
1. Now works with Python 3
2. Takes more general input texts (not just Project Gutenburg)
3. Now set up as a Markov object to be more flexible

TO ADD:
1. Way to import / export Markov suffix_map to save results and limit future
processing time
2. Way to merge results from multiple Markov's

"""

import sys
import random
from bisect import bisect


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.

    This could be made faster by computing the cumulative frequencies
    once and reusing them.
    """
    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    return words[index]


class Markov(object):
    """Markov object for creating one or more Markov generators"""
    def __init__(self, filename="", order=2):
        self.filename = filename
        self.order = order
        self.suffix_map = {}
        self.prefix = ()

        self.process_file()

    def process_word(self, word):
        """Processes each word in a file.

        word: string

        During the first few iterations, all we do is store up the words;
        after that we start adding entries to the dictionary.
        """
        self.prefix
        if len(self.prefix) < self.order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix][word] = \
                self.suffix_map[self.prefix].get(word, 0) + 1
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = {word: 1}

        self.prefix = shift(self.prefix, word)

    def process_file(self):
        """Reads the file of the Markov object and performs Markov analysis.

        Returns: map from prefix to list of possible suffixes.
        """
        fp = open(self.filename)

        for line in fp:
            for word in line.rstrip().split():
                self.process_word(word)

    def random_text(self, n=100):
        """Generates random wordsfrom the analyzed text.

        Starts with a random prefix from the dictionary.

        n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(list(self.suffix_map.keys()))

        for i in range(n):
            suffixDict = self.suffix_map.get(start, None)
            if suffixDict is None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                self.random_text(n-i)
                return

            # choose a random suffix
            word = random_word(suffixDict)
            print(word, end=" ")
            start = shift(start, word)

        print("")


def runMarkov(filename='', n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except:
        print('Usage: markov.py filename [# of words] [prefix length]')
    else:
        myMarkov = Markov(filename, order)
        myMarkov.random_text(n)

if __name__ == "__main__":
    runMarkov(sys.argv[1], sys.argv[2], sys.argv[3])
