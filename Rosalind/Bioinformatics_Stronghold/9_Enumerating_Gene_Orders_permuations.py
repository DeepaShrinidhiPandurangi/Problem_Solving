#9. Enumeraing gene orders : Permutations

'''
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
'''

# Using inbuilt function
from itertools import permutations
# permutations() takes an iterable datatype :str or list as an argument
a = 7
res = []
count=0
for i in range(1,a+1):
  res.append(str(i)) # the res should either be a string/list
  perm = permutations(res)


for i in list(perm):
  print(*i)
  count =count+1
print(count)
  

