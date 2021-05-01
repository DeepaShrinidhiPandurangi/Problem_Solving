#Phonebook
'''Objective 
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of 
names to query your phone book for. 
For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.
Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format

The first line contains an integer,n , denoting the number of entries in the phone book. 
Each of the n subsequent lines describes an entry in the form of 2  space-separated values on a single line. The first value is a friend's name, and the second value is an 8-digit phone number.
After the n  lines of phone book entries, there are an unknown number of lines of queries. 
Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.
Note: Names consist of lowercase English alphabetic letters and are first names only.

Constraints
1<=n <= 10^5
1<=queries<= 10^5
Output Format
On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise, print the full name and phoneNumber  in the format name=phoneNumber.
Sample Input
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output
sam=99912222
Not found
harry=12299933'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
# 1. If you want to accept all input queries together and give a combined o/p
n = int(input("enter the number of entries in the phonebook \n"))
list1 =[]
for i in range (0,n):
  name = list(map(str,input("enter the name follwed by ph.no.separated by spaces \n").split()))
  list1.extend(name)
#print(list1)
if len(list1)==0 or len(list1)== 1:
  print("no entries in the phone book")
else:
  phonebook={}
  for i,j in enumerate(list1):
    if i%2 ==0 :
      phonebook[j] = int(list1[i+1])
  print(phonebook)
#queries
queries = int(input("enter the number of queries"))
list2 =[]
for i in range (0,queries):
  query = list(map(str,input("enter the name to be searched in the phonebook ").split()))
  list2.extend(query)
print (list2)
for i,j in enumerate(list2):
  if j not in phonebook.keys():
    print('Not found')
  else:
    key = list(phonebook)[i]
    value = list(phonebook.values())[i]
    print(key,"=",value)


#2. 
# If you don't want to convert queries into list and give o/p after every i/p:
n = int(input("enter the number of entries in the phonebook \n"))
list1 =[]
for i in range (0,n):
  name = list(map(str,input("enter the name follwed by ph.no.separated by spaces \n").split()))
  list1.extend(name)
#print(list1)
phonebook={}
for i,j in enumerate(list1):
  if i%2 ==0 :
    phonebook[j] = int(list1[i+1])
#print(phonebook)
#from sys import stdin ( q range given )
for queries in range (1,1000000): #range given by Hackkerank
  q = input(" ")
  if q not in phonebook.keys():
    print('Not found')
  else:
    key = phonebook[q]
    print(str(q)+ "=" + str(key))
 
###### My final solution on Hackerrank
 #Better solution :(Note : you need not mention the range of query
 # excetion handling 
n = int(input("enter the number of entries in the phonebook \n"))
list1 =[]
for i in range (0,n):
  name1 = list(map(str,input("enter the name follwed by ph.no.separated by a space \n").split()))
  list1.extend(name1)
  phonebook={}
  for i,j in enumerate(list1):
    if i%2 ==0 :
      phonebook[j] = int(list1[i+1])
print(phonebook)

# read input till it is given , with Exception handling
while True: # while(1):

  try:
      name = input("enter thr number you want to search in the phone book")
      if name in phonebook:
        print(name+"="+str(phonebook[name]))
      else:
        print('Not found')
  except:
      break


 
 ### Hackerrank solution
n = int(input())
name_numbers = [input().split() for i in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break


