#Unique elements of a list
input= [1,2,1,2,1,3,2]
unique=[]
# To find out uniue elements of a list
for i in input:
    if i not in unique:
        unique.append(i)
print(unique)

#or
for i,j in enumerate(input):
    if j not in unique:
        unique.append(j)
print(unique)

#or
for i,j in enumerate(input):
    if j not in unique:
        unique.append(input[i])
print(unique)

#or
for i,j in enumerate(input):
    if j not in unique:
        unique.extend(input[i])
print(unique)