# String split

#****** Note: to split the sting of words into 2, the parameter maxsplit should be 1. (n-1) where n is the number of final pieces expected"
# Code 1
ext = 'geeks for geeks'
  
# Splits at space 
print(text.split()) 
  
word = 'geeks, for, geeks'
  
# Splits at ',' 
print(word.split(', ')) 
  
word = 'geeks:for:geeks'
  
# Splitting at ':' 
print(word.split(':')) 
  
word = 'CatBatSatFatOr'
  
# Splitting at 3 
print([word[i:i+3] for i in range(0, len(word), 3)]) 


'''
Output :

['geeks', 'for', 'geeks']
['geeks', 'for', 'geeks']
['geeks', 'for', 'geeks']
['Cat', 'Bat', 'Sat', 'Fat', 'Or']
'''

# Code 2
word = 'geeks, for, geeks, pawan'
  
# maxsplit: 0 
print(word.split(', ', 0)) 
  
# maxsplit: 4 
print(word.split(', ', 4)) 
  
# maxsplit: 1 
print(word.split(', ', 1)) 
Output :

['geeks, for, geeks, pawan']
['geeks', 'for', 'geeks', 'pawan']
['geeks', 'for, geeks, pawan']

# eg:
s = "deepa says hello world"
s= s.split(" ",2)
print(s)

# o/p: ['deepa', 'says', 'hello world']
