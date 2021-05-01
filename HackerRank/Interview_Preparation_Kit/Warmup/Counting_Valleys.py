# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

L = list("DDUUDDUDUUUD")
print(L)
counter = 0
L1 = []
for i in range(0,len(L)):
    counter1 = 0
    if L[i] == "U":
        counter += 1
    else:
        counter -= 1
    L1.append(counter)
print(L1)
ind = []
for i in range(0,len(L1)):
    if L1[i]==0:
        ind.append(i)
print(ind)
    
# For the valleys , take the counter values. count the zeros only below the origin. Any zeros above the origin are not of any use. Below origin ,the values are only negative. So, when you encounter a 0, check if the previous value is in valley i.e. negative.
valley = 0
for i in range(0,len(ind)):
    if L1[ind[i]-1] < 0:
        valley +=1
print(valley)


'''In the website'''

# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    L = list(path)
    #print(L)
    counter = 0
    L1 = []
    for i in range(0,len(L)):
        counter1 = 0
        if L[i] == "U":
            counter += 1
        else:
            counter -= 1
        L1.append(counter)
    #print(L1)
    ind = []
    for i in range(0,len(L1)):
        if L1[i]==0:
            ind.append(i)
    #print(ind)
        
    valley = 0
    for i in range(0,len(ind)):
        if L1[ind[i]-1] < 0:
            valley +=1
    return(valley)
