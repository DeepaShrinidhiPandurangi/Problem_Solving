s = "Able was I ere I saw Elba"
# s= "malayalam"
s = s.lower()

def ispalindrome(s):
  if len(s)==1 or len(s)== 2:
    return s[0]==s[-1]
  elif s[0]==s[len(s)-1]:
     return ispalindrome(s[1:len(s)-1])
  else:
    return False

print(ispalindrome(s))