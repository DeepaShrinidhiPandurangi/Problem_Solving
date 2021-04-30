# Dictionary
# output continuous key and values from  a dictionary
import string
dict = {}
alpha = string.ascii_lowercase
for i,j in enumerate(alpha):
	dict[j] = i+1
print (dict)
for i in range(0,len(dict)):
  key = list(dict)[i]  # or list(dict.keys())[i]   , make a list from the dictionary keys, then output the value of the given index
  value = list(dict.values())[i]
  print(key,"=",value)
'''more simple last 4 lines alternative :
for key,value in dict.items():
  print(key,"=",value)
'''
  

  
'''
output:
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 
'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26
'''

# Print all keys and values of a dictionary separately
import string
dict = {}
alpha = string.ascii_lowercase
for i,j in enumerate(alpha):
	dict[j] = i+1
#print (dict)
for i in range(0,len(dict)):
  key = dict.keys()
  value = dict.values()
print(key,value)
'''output:
dict_keys(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']) 
dict_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
'''

# 
import string
dict = {}
alpha = string.ascii_lowercase
letter = str(input(""))
for i,j in enumerate(alpha):
	dict[j] = i+1
#print (dict)
print(dict[letter] #  dict[key] = value ... fetch keys' individual values


# Print values in a certain way
s= "We tried list and we tried dicts also we tried Zen"
s= s.split()
print(s)
Dict = dict()
for i,j in enumerate(s):
  Dict[j] = s.count(j)
print(Dict)
for key,value in Dict.items(): # Prints key and value without any quotes
  print(key,value)
''' o/p:
['We', 'tried', 'list', 'and', 'we', 'tried', 'dicts', 'also','we', 'tried', 'Zen']
{'We': 1, 'tried': 3, 'list': 1, 'and': 1, 'we': 2, 'dicts': 1, 'also': 1, 'Zen': 1}
We 1
tried 3
list 1
and 1
we 2
dicts 1
also 1
Zen 1
'''