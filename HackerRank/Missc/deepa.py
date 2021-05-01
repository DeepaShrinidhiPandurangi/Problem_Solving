L = [1,5,4,3,2]
print(L)
L1 = L[:]
add= []
L_sort = sorted(L)
#print(L_sort)
N = len(L)
L_pos =[]
if L == L_sort:
  print(0)
else:
  for i in range (0,len(L)):
    if len(L) > 1:
      if L[i] != L_sort[i]:
        #Swap_flag = True
        while len(L1)>1:
          temp = L1[i]
          L1.remove(L1[i])
          print(L1)
          for i in range (0,len(L1)):
            if L[i] > min(L1):
              temp1 = L[i]
              for j in range(0,len(L1)):
                if L[j] == min(L1):
                  print(j)
                  res=j
                  L[j] = temp1
                  L[i] = min(L1)
                  L1[j-1]= temp1
                  print(L)
                  print(L1)            
  print(res)


# yesterday
L = [1,7,5,4,8,6,9]
print(L)
L_sort = sorted(L)
print(L_sort)

# indices
L_indices = []
L_sort_indices = []
for i in range (0, len(L_sort)):
  L_indices.append(i)
print(L_indices)
ind=0
for i,j in enumerate(L):
  ind = L_sort.index(j)
  L_sort_indices.append(ind)
print(L_sort_indices)

L_to_sort =[]
for i in L_indices:
  if L_indices[i]!= L_sort_indices[i]:
    L_to_sort.append(L_sort_indices[i])
print(L_to_sort)
L1 = L_to_sort
print(L1)

while len(L1) ==1:
  for i in range (0,len(L1)):
    temp = L1[i]
    if L1[i] > min[L1]:
      L1[i]= temp
      


//////
L = [1,7,5,4,8,6,9]
print(L)
L_sort = sorted(L)
print(L_sort)

L_to_sort =[]
for i in range (0,len(L)):
  if L[i]!= L_sort[i]:
    L_to_sort.append(L[i])
print(L_to_sort)
L1 = L_to_sort
print(L1)

swap_count =0

temp = L1[0]
while len(L1)>1:
  if L1[0] > min(L1):
    ind = L1.index(min(L1))
    L1[0]= min(L1)
    L1[ind]= temp
    L1.remove(L1[0])
    swap_count= swap_count+1
  else:
    L1[1] = L1[1]
print(L1)
print(swap_count)

##
L = [9,4,2,5,1,3,8]
print(L)
L_sort = sorted(L)
print(L_sort)

L_to_sort =[]
for i in range (0,len(L)):
  if L[i]!= L_sort[i]:
    L_to_sort.append(L[i])
print(L_to_sort)
L1 = L_to_sort

print("**",L1)

swap_count =0
print(sorted(L1))

temp = L1[0]
for i in range(0,len(L1)):
  if len(L1) == 1:
    L1[0] = L1[0]
  while L1 != sorted(L1):
    if L1[0] > min(L1):
      ind = L1.index(min(L1))
      L1[0]= min(L1)
      L1[ind]= temp
      swap_count= swap_count+1
      L1.remove(L1[0])

print(L1)
print(swap_count)

#1,7,5,4,8,6,9
      
      


