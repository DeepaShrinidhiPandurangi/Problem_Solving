from collections import defaultdict
nums = [1,2,3,1,1,3]
#nums = [1,1,1,1]
D = defaultdict(list)
for i in range(0,len(nums)):
  D[nums[i]].append(i)

#print(D)

sum = 0
for k,v in D.items():
  a = len(v)
  if a>1:
    sum = sum + (a*(a-1)//2)
print (sum)

''' #Brute Force

L = []
for i in range(0,len(nums)):
  for j in range(i+1,len(nums)):
    if nums[i] == nums[j]:
      if i<j:
        L.append((i,j))
return(len(L))
'''