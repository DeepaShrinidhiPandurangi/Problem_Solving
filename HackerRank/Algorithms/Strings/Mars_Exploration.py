# Mars Exploration
# Learn slicing by modulo


s = "SOSOOSOSOSOSOSSOSOSOSOSOSOS"

c = "SOS"
L = []
for i in range(0,len(s),3):
  if len(s[i:i+3]) == 3:
    L.append(s[i:i+3])
#print(L)

count=0
for i in L:
  for j,k in enumerate(i):
    if k != c[j]:
      count+=1
print(count)

'''
# Very nice way of solving : Hackkerrank solution
def marsExploration(s):
    return sum(s[i] != "SOS"[i%3] for i in range(len(s)))  #slicing by modulo
'''
