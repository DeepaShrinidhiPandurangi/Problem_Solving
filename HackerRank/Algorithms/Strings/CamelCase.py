# CamelCase
'''
There is a sequence of words in CamelCase as a string of letters,s , having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given , determine the number of words in .
Example :oneTwoThree

There are  words in the string: 'one', 'Two', 'Three'.

Function Description
Complete the camelcase function in the editor below.
camelcase has the following parameter(s):

string s: the string to analyze
Returns
int: the number of words in 
Input Format
A single line containing string . 

Constraints : string len greater than 1, less than 10^5
Sample Input
saveChangesInTheEditor

Sample Output
5 
'''

import string
s = "saveChangesInTheEditor"
if len(s) == 0:
  print(0)
else:
  count = 1
  for i in range(0,len(s)):
    if s[i] in string.ascii_uppercase:  # The other way (searching a smaller string in bigger one doesn't work.
      count+=1
print(count)



#  Using regex
import sys
import re

s = input().strip()
print(len(re.findall(r'[A-Z]', s)) + 1)