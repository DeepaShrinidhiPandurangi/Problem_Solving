'''Pangram:'''
import string
s= input("")
s= s.lower()
list=[]
#print(s)
a= string.ascii_lowercase
#print(a)
for i,j in enumerate(a):
  if j in s:
    #print("y")
    list.append("y")
  else:
    #print("n")
    list.append("n")
#print(list)

y= list.count("y")
#print(y)
n= list.count("n")
#print(n)

if y ==26:
  print("pangram")
elif n>=1:
  print("not pangram")


#Second and better code:
import string
t= int(input("Enter the Number of sentences:"))
for i in range(0,t):
    s= str(input("Enter the Sentence:"))
    s= s.lower()
    counter=0
    alphabets= string.ascii_lowercase
    #print(alphabets)
    for j,k in enumerate(alphabets):
        if k in s:
            counter= counter+1
    if counter == 26:
        print("This sentence is a pangram")
    else:
        print("This sentence is not a pangram")
    

