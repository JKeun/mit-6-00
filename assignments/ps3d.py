from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings
indices = '012345678901234567890123'
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExact(target, key):
    """return exact substring matches start points"""
    matches = ()
    start = 0
    while target.find(key, start) != -1:
        start = target.find(key, start)
        matches += (start,)
        start += 1
        # print(start)
    return matches

# print(subStringMatchExact(target1, key10))

### the following procedure you will use in Problem 3

def constrainedMatchPair(firstMatch, secondMatch, length):
    answers = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                answers += (n,)
    return answers


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print('breaking key',key,'into',key1,key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print('match1',match1)
        print('match2',match2)
        print('possible matches for',key1,key2,'start at',filtered)
    return allAnswers
        

def subStringMatchExactlyOneSub(key, target):
    """ return a tuple of all starting points of matches of the key to
        the target, such that at exactly one element of the key is incorrectly matched to the target."""
    possible_answers = subStringMatchOneSub(key, target)
    exact_answers = subStringMatchExact(target, key)
    answers = ()
    for answer in possible_answers:
        if not answer in exact_answers:
            answers += (answer,)
    return answers

print(subStringMatchExactlyOneSub(key12, target1))