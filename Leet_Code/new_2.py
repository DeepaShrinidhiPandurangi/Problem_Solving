s= 10011000011100011110111111100000011111
s= str(s)
print(s)
c = 0
temp= 0
L=[]
for i in range(0,len(s)):
	if s[i]=="1":
		c = c+1
		
	else:
		c = 0
	temp= (max(temp,c))
	L.append(temp)
print(L)
	
