# Caesar Cipher
import string
s = "Hello_World!"
k= 4
k = k%26 # Do not change value when k < len(s) but once more, make k = k % 26 to get the remainder
'''
lower_case = string.ascii_lowercase
shift_lower_case = lower_case[k:] + lower_case[:k]
upper_case = string.ascii_uppercase
shift_upper_case = upper_case[k:] + upper_case[:k]

letters = lower_case + upper_case
shifted_letters = shift_lower_case + shift_upper_case

D = {}
for i,j in enumerate(letters):
  D[j] = shifted_letters[i]
#print(D)
'''
letters = string.ascii_letters
shifted = letters[k:26]+letters[:k] + letters[26+k:] + letters[26:26+k]
#print(shifted)
D = {}
for i,j in enumerate(letters):
  D[j] = shifted[i]
#print(D)

res=""
for i,j in enumerate(s):
  if j in string.ascii_letters:
    res =  res + D[j]
  else:
    res = res + j

print(res)
  
  






  

