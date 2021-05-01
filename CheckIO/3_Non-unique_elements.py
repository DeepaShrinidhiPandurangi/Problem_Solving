#Non-unique elements
'''
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. 
To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
'''

def checkio(data: list) -> list:
  L_dict ={}
  L_dist =[]
  for i in data:
    if i not in L_dist:
      L_dist.append(i)
  if data== L_dist:
    return []
  else:
    for i,j in enumerate(data):
      L_dict[j] = data.count(j)

    for key,value in L_dict.items():
      if value == 1:
        data.remove(key)
    return (data)
    
    
print(checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3])
print(checkio([1, 2, 3, 4, 5]) == [])
print(checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])
print(checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9])