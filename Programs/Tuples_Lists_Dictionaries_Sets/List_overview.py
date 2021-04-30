# List operations

# Iterating over a list
s = 'azcb' #"zyxscba"
ind = []
for i in range(0,len(s)-1):
  print(s[i+1],s[i])
'''
o/p:
z a
c z
b c
'''

#Lists in Python at a glance:
list1 = []                      # A new empty list
list2 = [1, 2, 3, "cat"]        # A new non-empty list with mixed item types
list1.append("cat")             # Add a single member, at the end of the list
list1.extend(["dog", "mouse"])  # Add several members
list1.insert(0, "fly")          # Insert at the beginning
list1[0:0] = ["cow", "doe"]     # Add members at the beginning
doe = list1.pop(1)              # Remove item at index
if "cat" in list1:              # Membership test
  list1.remove("cat")           # Remove AKA delete
#list1.remove("elephant") - throws an error
for item in list1:              # Iteration AKA for each item
  print item
print "Item count:", len(list1) # Length AKA size AKA item count
list3 = [6, 7, 8, 9]
for i in range(0, len(list3)):  # Read-write iteration AKA for each item
  list3[i] += 1                 # Item access AKA element access by index
last = list3[-1]                # Last item
nextToLast = list3[-2]          # Next-to-last item
isempty = len(list3) == 0       # Test for emptiness
set1 = set(["cat", "dog"])      # Initialize set from a list
list4 = list(set1)              # Get a list from a set
list5 = list4[:]                # A shallow list copy
list4equal5 = list4==list5      # True: same by value
list4refEqual5 = list4 is list5 # False: not same by reference
list6 = list4[:]
del list6[:]                    # Clear AKA empty AKA erase
list7 = [1, 2] + [2, 3, 4]      # Concatenation
print list1, list2, list3, list4, list5, list6, list7
print list4equal5, list4refEqual5
print list3[1:3], list3[1:], list3[:2] # Slices
print max(list3 ), min(list3 ), sum(list3) # Aggregates

print [x for x in range(10)]    # List comprehension
print [x for x in range(10) if x % 2 == 1]
print [x for x in range(10) if x % 2 == 1 if x < 5]
print [x + 1 for x in range(10) if x % 2 == 1]
print [x + y for x in '123' for y in 'abc']

# More:
https://en.wikibooks.org/wiki/Python_Programming/Lists