import numpy
def unique_in_order(s):
 i=0
 list=[]
 while i < len(s):
  list.append(s[i])
  i=i+1
 a=numpy.unique(list)
 print(a)
 return
unique_in_order("AAAA")
