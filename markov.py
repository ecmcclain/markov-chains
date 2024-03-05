"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as file:
        text = file.read().replace('\n', " ")

    return text

#open_text = open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    #turn input string into list
    words_list = text_string.strip().split(" ")

    #iterate through the list word by word
    for index, word in enumerate(words_list):
        #if the current word and the next word are in the dictionary, append the next next word to the value list
        #otherwise, add the current word and next word tuple with the next next word value to the dictionary
        if index < len(words_list) -2:
            temp_tuple = (word, words_list[index+1])
            temp_list = chains.get(temp_tuple, list())
            temp_list.append(words_list[index+2])
            chains[temp_tuple] = temp_list
   
    return chains
"""
dictionary = make_chains(open_text)
for word, values in dictionary.items():
    print(f'{word}: {values}')
    """


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    #get a link using choice on list(chains.keys())
    link = choice(list(chains.keys()))

    ## start of repeat
    #check if the next key is in chains
    while link in chains:
        #add the link to the words list
        words.append(link[0])

        #get the list of valid words for the link
         #select the next word using choice on the list of valid words
        next_word = choice(chains[link])

        #make the next key out of the second part of the link
        link = (link[1], next_word)
    #repeat 
    #add the key that not in the dictionary to the words list
    words.extend([link[0], link[1]])

    return ' '.join(words)

#print(make_text(dictionary))

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)



