from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


def subStringMatchExact(target, key):
    matches = ()
    start = 0
    while target.find(key, start) != -1:
        cur_match = target.find(key, start)
        matches += (cur_match, )
        start += cur_match + 1
    return matches


print(subStringMatchExact(target1, key10))
print(subStringMatchExact(target1, key11))
print(subStringMatchExact(target1, key12))
print(subStringMatchExact(target1, key13))
print(subStringMatchExact(target2, key10))
print(subStringMatchExact(target2, key11))
print(subStringMatchExact(target2, key12))
print(subStringMatchExact(target2, key13))