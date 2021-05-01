def encrypt_this(text):
  L = text.split(" ")
  L1=[]
  for i in L:
    if len(i) == 0:
      st = ""
    elif len(i) == 1:
      st = str(ord(i[0]))
    elif len(i) == 2:
      st = str(ord(i[0]))+i[-1]
    elif len(i)== 3:
      st = str(ord(i[0]))+i[-1]+i[1]
    else:
      st = str(ord(i[0]))+i[-1]+i[2:-1]+i[1]
    L1.append(st)
  #print(L1)
  fin=""
  res=""
  for i in L1:
    if len(L1)==1:
      res = i
    else:
      fin = fin+" "+i
      res = fin[1::]
  return(res)
'''
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''
