L = [2,5,8,3,1,9]
print(L)
L1 = L[:]
L_sort = sorted(L)
#print(L_sort)
N = len(L)
#while len(L1)>1:
for i in range (0,len(L)):
  if L[i] != L_sort[i]:
    temp = L1[0]
    print ("temp","=",temp)
    temp1 = L[i]
    L1.remove(L1[0])
    print(L1)
    if L[i] > min(L1):
      for j in range(0,len(L1)):
        if L1[j] == min(L1):
          print(j)
          L[j+1] = temp1
          L[i] = min(L1)
          L1[j] = temp1
          print(L)
          print(L1)            

