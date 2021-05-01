S = "19998533444455"
temp = 0 
count = 0
num= []
ind=[]
ind.append(-1)
for i in range(0,len(S)-1):
  if S[i]!=S[i+1]:
    num.append(S[i])
    ind.append(i)
num.append(S[-1])
ind.append(len(S)-1)
ind1=[]
for i in range(0,len(ind)-1):
  ind1.append(ind[i+1]-ind[i])
res = [(int(a),b)for a,b in zip(num,ind1)]
print(*res)


# Try to do this using itertools groupby
from itertools import groupby
for k,g in groupby(S):
  grp = []
  #a=(int(k),list(g))                                  
  #print(a)														
  a = (int(k),len(list(g)))
  print(a,end=" ")
	
'''														(1, ['1'])
														(9, ['9', '9', '9'])
														(8, ['8'])
														(5, ['5'])
														(3, ['3', '3'])
														(4, ['4', '4', '4', '4'])
														(5, ['5', '5'])
										'''