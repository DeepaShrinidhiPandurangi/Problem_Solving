import numpy
def unique_in_order(s):
 i=0
 list=[]
 while i < len(s):
  list.append(s[i])
  i=i+1
 if len(numpy.unique(list)) == 1:
  print("repeated")
 else:
  print("unique")
unique_in_order("AAAA")
unique_in_order("AAAAB")
