#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
 
# Complete the checkMagazine function below.  #Note : *********** This function takes a lot of time and causes timeout error when solved like this.as creation of a dictionary using "count" takes lots of time.
#Solve it using Collections Counter() and set theory.

def checkMagazine(magazine, note):
    #print(magazine,note)
    D_Mag = {}
    D_Note = {}

    for i in range(0,len(magazine)):
        D_Mag[magazine[i]] = magazine.count(magazine[i])

    for i in range(0,len(note)):
        D_Note[note[i]] = note.count(note[i])

    #print(D_Mag)
    #print(D_Note)

    Yes_count = 0
    for key,value in D_Note.items():
        if key in D_Mag and value <= D_Mag[key]:
            Yes_count+=1
    if Yes_count == n:
        print("Yes")
    else:
        print("No")

		
'''
#Complete the checkMagazine function below.

# a intersection b should give you b. a is the bigger set. 
a&b = a intersection b
a|b = a union b
a - b = a minus b 
b - a = b minus a
a ^ b = symmetric difference (a-b) union (b-a)


def checkMagazine(magazine, note):
    a = Counter(magazine)
    b = Counter(note)
    if a&b == b:
        print("Yes")
    else:
        print("No")
'''

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
	
	
'''
class collections.Counter([iterable-or-mapping])¶

**** A counter tool is provided to support convenient and rapid tallies.****


A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

Elements are counted from an iterable or initialized from another mapping (or counter):

>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args
Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a KeyError:

>>> c = Counter(['eggs', 'ham'])
>>> c['bacon']                              # count of a missing element is zero
0
Setting a count to zero does not remove an element from a counter. Use del to remove it entirely:

>>> c['sausage'] = 0                        # counter entry with a zero count
>>> del c['sausage']                        # del actually removes the entry
'''
