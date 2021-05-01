#L=[1,2,3,4,5]
#L = [9,4,2,5,1,3,8]
L=[5,4,9,1,2,6]
#L= [4,2,5,1,3,8]
#L = [1,5,4,3,2]
#L = [1,2]
#L =[1,2,3]
#L=[]
swap_count =0
print(L)
L_sort= sorted(L)
if L == sorted(L):
  swap_count= 0
else:
  L_to_sort =[]
  for i in range (0,len(L)):
    if L[i]!= L_sort[i]:
      L_to_sort.append(L[i])
  print(L_to_sort)
  L1 = L_to_sort

  print("**",L1)
  print(sorted(L1))

  if len(L1) == 1:
    L1[0] = L1[0]
  else:
    while L1!= L_sort :
      temp =L1[0]
      if len(L1) == 1:
        break
      if L1[0] > min(L1):
        ind = L1.index(min(L1))
        L1[0]= min(L1)
        L1[ind]= temp
        swap_count=swap_count+1
        L1.remove(L1[0])
        L_sort.remove(L_sort[0])
        print(";;",L_sort)
        print(L1)
      else :
        L1= L1
        break

print(swap_count)

# L= [1,7,5,4,8,6,9]
#L= [4,2,5,1,3,8]
      
      


