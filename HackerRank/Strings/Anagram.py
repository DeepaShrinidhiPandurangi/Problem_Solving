'''Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?
Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make  a and b anagrams. Any characters can be deleted from either of the strings.
For example, if a=cde  and b=dcf , we can delete e from a string  and f from b string  so that both remaining strings are cd and  dc which are anagrams.
Function Description
Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.

makeAnagram has the following parameter(s):
a: a string
b: a string

Input Format
The first line contains a single string, . 
The second line contains a single string, .

Constraints
The strings  and  consist of lowercase English alphabetic letters ascii[a-z].

Output Format
Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input
cde
abc

Sample Output
4 

We delete the following characters from our two strings to turn them into anagrams of each other:
Remove d and e from cde to get c.
Remove a and b from abc to get c.
We must delete  characters to make both strings anagrams, so we print  on a new line.'''

def makeAnagram(a, b):
  #import numpy as np
  cuta =""
  cutb =""
  for i in a:
    if i not in b:
      cuta = cuta + i
  for i in b:
    if i not in a:
      cutb = cutb + i

  res1 = len(cuta) + len(cutb)
  res2=0
  
# update the strings after cuts
  for i in a:
    if i in cuta:
      a= a.replace(i,'')
      a=''.join(sorted(a))
    else:
      a=''.join(sorted(a))
  for i in b:
    if i in cutb:
      b= b.replace(i,'')
      b=''.join(sorted(b))
    else:
      b=''.join(sorted(b))

  #sort a and b strings in ascending order
  dicta = {}
  for i,j in enumerate(a):
    dicta[j] = a.count(j)

  dictb = {}
  for i,j in enumerate(b):
    dictb[j] = b.count(j)

#return (dicta,dictb)
  lista=[]
  for key,value in dicta.items():
    lista.append(value)

  listb=[]
  for key,value in dictb.items():
    listb.append(value)

  ## if numpy is used
  #lista = np.array(lista)
  #listb = np.array(listb)
  #listc= abs(lista-listb)

# subtract corresponding elements of 2 lists
  listc = [abs(a - b) for a, b in zip(lista, listb)]

  count= 0
  for i in listc:
    res2= res2 + i

  return (res1+res2)
  


print(makeAnagram("abcd","bcde"))
print(makeAnagram("ssabcd", "sssabeda"))
print(makeAnagram("abcd", "abcdd"))
print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))


# Second method
def makeAnagram(a, b):
  res = 0  
  import string
  #arrange the alphabets in ascending order
  a=''.join(sorted(a)) # not needed
  b=''.join(sorted(b)) # not needed
  # lower case alphabets 
  alpha = string.ascii_lowercase
  #make a dictionary with the count of corresponding alphabets from the lowercase       alphabets in string a and string b
  dicta = {}
  for i,j in enumerate(alpha):
    dicta[j] = a.count(j)
  dictb = {}
  for i,j in enumerate(alpha):
    dictb[j] = b.count(j)
#return (dicta,dictb)
#make a list of values of keys from lista and listb corres. to string a and string b
  lista=[]
  for key,value in dicta.items():
    lista.append(value)
  listb=[]
  for key,value in dictb.items():
    listb.append(value)
# subtract corresponding elements of 2 lists
  listc = [abs(a - b) for a, b in zip(lista, listb)]
  count= 0
  for i in listc:
    res= res + i
  return (res)
