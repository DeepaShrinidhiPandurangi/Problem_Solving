from itertools import permutations
S = list(map(str,input().split()))
s = S[0]
n = int(S[1])
L= sorted(list(permutations(s,n)))
for i in L:
  res = ""
  for j in range(0,len(i)):
    res = res + i[j]
  print(res)

from itertools import combinations
S = list(map(str,input().split()))
s = sorted(S[0]) # sort here
n = int(S[1])
for k in range(1,n+1):
    L= list(combinations(s,k))
    for i in L:
        res = ""
        for j in range(0,len(i)):
            res = res + i[j]
        print(res)
