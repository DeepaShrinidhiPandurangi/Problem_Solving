rnk# Collections: defaultdict

L = [1,2,3,4,1,2,3,4,1,1,1,1,8]
from collections import defaultdict
d = defaultdict(list)
d1 = defaultdict(list)
for i,j in enumerate(L):
  d[j] = L.count(j)
  d1[j].append(i)


print(d)
print(d1)


print(d.items())
print(d1.items())
