# 6.00 Problem Set 6
#
# The 6.00 Word Game
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

def get_words_to_points(word_list):
    """
    Return a dict that maps every word in word_list to its point value. 
    """
    words_to_points = {}
    for word in word_list:
        words_to_points[word] = get_word_score(word, HAND_SIZE)
    return words_to_points

def get_word_rearrangements(word_list):
    # pseudocode
    
    # Let d = {}
    # For every word w in the word list:
        # Let d[(string containing the letters of w in sorted order)] = w

    d = {}
    for word in word_list:
        sorted_word = ""
        for letter in sorted(list(word)):
            sorted_word += letter
        d[sorted_word]= word
    return d
        
def get_time_limit(points_dict, k):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k 


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
    if len(word) == n:
        score += 50
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=" ")              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3)
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    freq = get_frequency_dict(word)
    newhand = {}
    for char in hand:
        newhand[char] = hand[char]-freq.get(char,0)
    return newhand
    #return dict( ( c, hand[c] - freq.get(c,0) ) for c in hand )
        

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the points_dict and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or points_dict.
    
    word: string
    hand: dictionary (string -> int)
    points_dict: dictionary of <lowercase strings, points>
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    
    # https://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity
    # in operation on a dict, or the dict_keys object you get back from calling keys() on it (in 3.x),
    # is not O(N), it's O(1).
    # The in operator, like most other operators, is just a call to a __contains__ method (or the equivalent for a C/Java/.NET/RPython builtin)
    # list implements it by iterating the list and comparing each element;
    # dict implements it by hashing the value and looking up the hash;
    return word in points_dict

def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made with the
    given hand.
    Return '.' if no words can be made with the given hand.
    """
    candidates = {}
    for word in points_dict:
        if is_valid_word(word, hand, points_dict):
            candidates[word] = points_dict[word]
    
    best_word = "."
    highest_point = 0
    for cand in candidates:
        if candidates[cand] > highest_point:
            best_word = cand
            highest_point = candidates[cand]

    return best_word

def pick_best_word_faster(hand, rearrange_dict):
    # pseudocode
        
    # To find some word that can be made out of the letters in HAND:
        # For each subset S of the letters of HAND:
            # Let w = (string containing the letters of S in sorted order)
            # If w in d:
                # return d[w]
    sorted_hand = ""
    for letter in sorted(list(hand)):
        if hand.get(letter) > 0:
            sorted_hand += letter
    
    subsets = []
    for i in range(len(sorted_hand)):
        subsets.append(sorted_hand[:i])
    # print(subsets)
    
    best_word = "."
    highest_point = 0
    for subset in subsets:
        if subset in rearrange_dict:
            point = get_word_score(subset, HAND_SIZE)
            if point > highest_point:
                best_word = rearrange_dict[subset]
                highest_point = point

    return best_word

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      points_dict: dictionary of <lowercase strings, points>
    """    
    total = 0
    initial_handlen = sum(hand.values())
    timeLimit = float(input("Enter time limit, in seconds, for players: "))
    total_time = 0
    while sum(hand.values()) > 0:
        print("Current Hand:", end="\t"), display_hand(hand), print()
        # start_time = time.time()
        # userWord = input('Enter word, or a . to indicate that you are finished: ')
        # userWord = pick_best_word(hand, points_dict)
        userWord = pick_best_word_faster(hand, rearrange_dict)
        print("Enter word, or a . to indicate that you are finished: ", userWord)
        # end_time = time.time()
        cur_time = time_limit
        print("It took %0.2f seconds to provide an answer." % cur_time)
        total_time += cur_time
        if timeLimit-total_time >= 0:
            print("You have %0.2f seconds remaining." % (timeLimit-total_time))
        else:
            print("Total time exceeds %0.2f seconds. Your scored %0.2f points" % (timeLimit, total))
            break
            
        if userWord == '.':
             break
        else:
            isValid = is_valid_word(userWord, hand, word_list)
            if not isValid:
                print("Invalid word, please try again.")
            else:
                points = get_word_score(userWord, initial_handlen)
                total += points / (cur_time+0.00001)
                print ('%s earned %d points. Total: %d points' % (userWord, points, total))
                hand = update_hand(hand, userWord)
    print ('Total score: %d points.' % total)


#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    time_limit = get_time_limit(points_dict, 50)
    rearrange_dict = get_word_rearrangements(word_list)
    play_game(word_list)
    
    
## Problem 5 ##
# your response here.
# as many lines as you want.
# 
# pick_best_word()
#   This method creates a dictionary of every valid word mapped to the point value.  Then it iterates through the dictionary comparing the hand to the word.
#   If they word can be made from the hand then the word's score is compared to the word score of the earlier possible word.  The higher score word is retained.
#   Under this method the point value dictionary must be built and then the function iterates through comparing the hand to eveyr possible word.
#   Amortizing the time-cost of building the dictionary over each pick, the time complexity of this method grows with the length of the word list and independently from the size of the hand.
#   Adding letters to the hand will increase the time to execute but only negligibly.  I think the computational complexity of the function is linear.
# 
#   With a hand size of 7 letters the time to pick best word was less than .6 seconds.
#   With a hand size of 17 letters the time to pick best word was ~.6 seconds.
#   With a hand size of 25 letters the time to pick best word was ~.65 seconds.



#     
# pick_best_word_faster()
#   This method also begins by creating a dictionary.  Each value in the dictioanry is a valid word.  Each key is a alphabetized string of the letters in the word. E.g., {'acot':'taco'}.
#   Note that each key is unique but the value isn't necessarily unique.  The dictionary value for 'acot' could be 'coat'.
#   This is because the dictionary only needs to list every valid alpahbetized string of letters.  Not ever valid word.
#   This makes the dictionary the same size or shorter than the dictionary created in pick_best_word().
#   For the word list used in this problem the savings is ~14,000 entries (83667 words, 69091 dict keys)
#   Armed with this dictionary the function can take advantage of the speed of the "in dictionary" function, which I thinks is logarithmic. 
#   The next part of this function is build a set of substrings of hand.  The function then iterates through this set of substrings checking if they are in the dictionary,
#   and comparing their point value to the prior highest value string in the dictionary.  The function returns the highest point value value from the dictionary.
#   This method is much faster than pick_best_word() because is takes adavantice of the bysect search functionality built into search dicstionaries.
#   This bysect search algorithm grow logarithmically based on the length of dictionary.
#   Adding letters to the hand will increase the time to execute the function that creates the subsets, but they dicitonary search is the more significant funciton.
#   I think the computational complexity of the function is logarithmic.

#   With a hand size of 7 letters the time to pick best word was less than .001 seconds.
#   With a hand size of 17 letters the time to pick best word was between .3 and .5 seconds.
#   With a hand size of 25 letters the time to pick best word was between 15 and 45 seconds.

#   Comparing the two functions, it appears the pick_best_word_faster() is much faster for relatively small hands and any size dictionary. 
#   But pick_best_word() is faster if the hands will be large.  Not surprisingly the 'better' function depends on the specifics of the problem.