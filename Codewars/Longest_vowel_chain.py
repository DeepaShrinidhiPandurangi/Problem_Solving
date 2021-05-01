#Longest vowel chain
'''The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.

Good luck!'''


def solve(s):
  L=[]
  st=""
  for i in range(0,len(s)):
    if s[i] in ["a","e","i","o","u"]:
      st=st + s[i]
      L.append(st)
    else:
      st=""
  return(len(max(L,key=len)))
  pass
