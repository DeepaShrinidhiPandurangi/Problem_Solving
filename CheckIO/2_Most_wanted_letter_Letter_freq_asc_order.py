# The most wanted Letter : Letter Frequency by ascending order

import string
def checkio(text):
  #Final string to work on
  text_check =""
  # Convert the string to lowercase
  text1 = text.lower()
  # remove spaces from the string
  text2 = text1.replace(" ","")
  # Revome all the digits and punctuation for the string
  for i,j in enumerate(text2):
    if j not in (string.punctuation):
      if j not in (string.digits):
        text_check = text_check + j
  text_check = sorted(text_check)
  L1 =[]
  L_dist =[]
  letter_dict ={}
  #replace this for solution
  for i,j in enumerate(text_check):
    letter_dict[j] = text_check.count(j)
  print(letter_dict)

  for key,value in letter_dict.items():
    L1.append(value)
  for i in L1:
    if i not in L_dist:
      L_dist.append(i)
  if len(L_dist) == 1:
    for key1,value1 in letter_dict.items():
      return (key1)

  for key,value in letter_dict.items():
    if value == max(letter_dict.values()):
      return (key)