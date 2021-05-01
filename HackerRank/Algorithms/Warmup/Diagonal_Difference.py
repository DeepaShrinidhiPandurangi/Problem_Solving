#Using Numpy

import numpy
 as np

a = np.array([[11, 2 ,4],[4, 5 ,6], [10, 8 ,-12]]) # primary diagonal
b = np.fliplr(a) # or np.flipud(a)                 #secondary diagonal
print(abs(np.trace(a)-np.trace(b)))

print(a)
print(b)
print(abs(a-b))


# Without using numpy

# Make an array
n = 3  # Number of rows of the matrix
arr = []
for i in range(0,n):
  arr.append(list(map(int,input("enter the numbers ").split())))
print(arr)

primary = sum([arr[i][i]for i in range(0,n)])
print(primary)
secondary =  sum([arr[i][n-i-1]for i in range(0,n)]) # Use iteration of i to subtract
print(secondary)

print(abs(primary-secondary))

