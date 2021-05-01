#Check if all the elements of the list are the same.
# Note : Print True if yes. Else print False. It is True if the number of elements are 0 or 1.


def all_the_same(List):
    # identify the distinct elements of the list. If the distinct elements > 1 , then the list elements are not equal
  List1 =[] # empty list, here we compare the given list to an empty list to get the distinct elements
  for i in List:
    if i not in List1:
      List1.append(i)
  if len(List1)> 1:
    return False
  else:
    return True       
	
print(all_the_same([1, 1, 1, 1]))
print(all_the_same([1, 2, 1 ,2]))
print(all_the_same(['b','a', 'a', 'a','b']))
print(all_the_same([]))
print(all_the_same(['c']))

	
	
# Soln.2
def all_the_same(List):
  count=0
  if len(List) == 0 or len(List) == 1:
    return True
  else:
    for i in range(0,len(List)):
      for j in range (0,len(List)):  #or (i+1,len(List))# if you set the range 0,i or 0,i+1 ,do not use break as it will terminate after i = 0
        if List[i]!= List[j]:   # left side element should remain the same,and compared with different right side elements .
          count = count+1
      break # Outer most loop break.Can break cause 1 iteration of i is enough.
    #print(count)
    if count == 0:
      return True
    else:
      return False

print(all_the_same([1, 1, 1, 1]))
print(all_the_same([1, 2, 1 ,2]))
print(all_the_same(['b','a', 'a', 'a','b']))
print(all_the_same([]))
print(all_the_same(['c']))

# To avoid break, the correct solution is:
def all_the_same(List):
  count=0
  if len(List) == 0 or len(List) == 1:
    return True
  else:
    for i in range(0,1): # i just one iteration
      for j in range (0,len(List)): 
        if List[i]!= List[j]:   # left side element should remain the same,and compared with different right side elements .
          count = count+1
    #print(count)
    if count == 0:
      return True
    else:
      return False
print(all_the_same([1, 1, 1, 1]))
print(all_the_same([1, 2, 1 ,2]))
print(all_the_same(['b','a', 'a', 'a','b']))
print(all_the_same([]))
print(all_the_same(['c']))

# Soln 3
# Check io soln
def all_the_same(elements):
    return all(x == y for x, y in zip(elements, elements[1:])) #The all() function returns True if all items in an iterable are true, otherwise it returns False.


print(all_the_same([1, 1, 1, 1]))
print(all_the_same([1, 2, 1 ,2]))
print(all_the_same(['b','a', 'a', 'a','b']))
print(all_the_same([]))
print(all_the_same(['c']))    
    
    
'''
o/p:
True
False
False
True
True
'''  


'''
L= [1,1,1,1]
print (all (a==b for a,b in zip(L,L[1:])))

The all() function returns True if all items in an iterable are true, otherwise it returns False. If the iterable object is empty, the all() function also returns True.  
'''
