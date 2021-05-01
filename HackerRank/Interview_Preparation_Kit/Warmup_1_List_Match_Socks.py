''' Warm-up 1:
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are n=7  socks with colors ar = [1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2 . 
There are three odd socks left, one of each color. The number of pairs is 2.
Function Description
Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock
Input Format
The first line contains an integer , the number of socks represented in . 
The second line contains  space-separated integers describing the colors  of the socks in the pile.
Constraints
1<=n<=100
1<=ar[i]<= 100 where 0<=i<=n
 where 
Output Format
Return the total number of matching pairs of socks that John can sell.
Sample Input
9
10 20 20 10 10 30 50 10 20
Sample Output
3
'''
# Without function
ar = list(map(int, input("Enter the integers with a space in between: ").split()))# Note this step. Converts input with spaces into list 
print(ar)
unique=[]
pairs=0
extras=0
# To find out unique elements of a list
for i,j in enumerate(ar):
    if j not in unique:
        unique.append(ar[i])
#print(unique)
for i,j in enumerate(unique):
    counter= ar.count(unique[i])
    #print("The count of",unique[i],"is:",counter)
    if counter%2 == 0:
        pairs = pairs+counter//2
    else:
        pairs= pairs+counter//2
        extras= extras+1
print(pairs)
print(extras)
    


'''
# The code that worked on the website:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique=[]
    pairs=0
    extras=0
# To find out uniue elements of a list
    for i,j in enumerate(ar):
        if j not in unique:
            unique.append(ar[i])
    #print(unique)
    for i,j in enumerate(unique):
        counter= ar.count(unique[i])
        #print("The count of",unique[i],"is:",counter)
        if counter%2 == 0:
            pairs = pairs+counter//2
        else:
            pairs= pairs+counter//2
            extras= extras+1
    return pairs
    #print(extras)
    
# Given by them:  ****Note this procedure****
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()'''


