# subtract corresponding elements of 2 lists
  listc = [abs(a - b) for a, b in zip(lista, listb)]  # it is a multilined program written in one line. [ ] needed. Inside all ().


#__________________________________________________________________________________________________________________________________________#
#Reverse a list
#method 1 : L.reverse()
L = [2,3,4,5]
L.reverse()  # Note : If you want to assign this to a variable , then use L2 = list(L1.reverse()). Explicitly tell that that variable is a list.
             # Declaring like this won't help. L2= [] , L2 = L1.reverse()
print(L)
'''
o/p: [5, 4, 3, 2]
'''

# method2 : reversed(L)
L1 = [6,3,4,5]
L2 = list(reversed(L1))
print(L1,L2)
'''
[6, 3, 4, 5] [5, 4, 3, 6]
'''

L = [2,3,4,5]
L1 = L[:]
L1.reverse() 
print(L,L1)
# o/p:[2, 3, 4, 5] [5, 4, 3, 2]
L = [2,3,4,5]
L1 = L[:]
L1 = list(reversed(L1))
print(L,L1)
# o/p:[2, 3, 4, 5] [5, 4, 3, 2]

# method 3 : reverse by indexing
L = [2,3,4,5]
print(L[::-1])
#o/p:[5, 4, 3, 2]

#______________________________________________________________________________________________________________________________________________#

# Indexing
L = [1,2,3,4]
print(L[0:]) # 0 to last
print(L[:0]) # 0 to 0
print(L[1:]) #1 to last
print(L[:1]) # 0 to 1
'''
o/p:
[1, 2, 3, 4]
[]
[2, 3, 4]
[1]
'''