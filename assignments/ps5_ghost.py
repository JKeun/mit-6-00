# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()


# TO DO: your code begins here!
def check_letter(letter):
    """
    Return letter when letter in string.ascii_letters otherwise None
    Args:
        letter: string
    """
    if letter not in string.ascii_letters:
        print("Invalid letter. please enter an alphabetic character again.")
        return None
    else:
        return letter.lower()

def validate_fragment(fragment, cur_user):
    """
    Returns boolean. after user input a letter, if there's fully matched word
    in wordlist or there's no any word starting current fragment,
    return False, otherwise True.
    Args:
        frag: string
    """
    if len(fragment) > 3 and fragment in wordlist:
        print(f"Player {cur_user} loses because '{fragment}' is a word!")
        return False
    
    matched = []
    for word in wordlist:
        matched.append(word[:len(fragment)] == fragment)
    if not any(matched):
        print(f"Player {cur_user} loses because no word begins with '{fragment}'!")
        return False
    
    return True

def ghost():
    print("Welcom to Ghost!")
    print("Player 1 goes first.")
    print("Current word fragment: ''")
    
    fragment = ""
    while True:
        cur_user = str(len(fragment) % 2 + 1)
        
        letter = check_letter(input(f"Player {cur_user} says letter: "))
        if letter:
            fragment += letter
            print()
            print(f"Current word fragment: '{fragment}'")
            
            if validate_fragment(fragment, cur_user):
                cur_user = str(len(fragment) % 2 + 1)
                print(f"Player {cur_user}'s turn.")
            else:
                cur_user = str(len(fragment) % 2 + 1)
                print(f"Player {cur_user} wins!")
                break

if __name__=="__main__":
    ghost()