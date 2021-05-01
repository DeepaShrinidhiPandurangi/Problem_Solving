a= "bugexikjevtubidpulaelsbcqlupwetzyzdvjphn"
b= "lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk"
s1=""
s2=""
s11=""
s22=""
count=0
e1=""
e2=""
count1=0
count2=0
#For characters in a not in b
for i in range(0,len(a)):
    if a[i] not in b:
        s1=s1+a[i]
#print(s1)
#For remaining characters in original string a
for i in range(0,len(a)):
    if a[i] not in s1:
        s11=s11+a[i]        
print(s11)
#For characters in b not in a
for i in range(0,len(b)):
    if b[i] not in a:
        s2=s2+b[i]
#print(s2)
#For remaining characters in original string b
for i in range(0,len(b)):
    if b[i] not in s2:
        s22=s22+b[i]
print(s22)
if len(s11)!=len(s22):
    #For characters-unique in original string a       
    for i in range(0,len(s11)):
        if s11[i] not in e1:
            e1=e1+s11[i]
    #print(e1)
    #For characters-unique in original string b    
    for i in range(0,len(s22)):
        if s22[i] not in e2:
            e2=e2+s22[i]
    #print(e2)
    # Note : len(e1) = len(e2)
    
    #####################correct from here
    # check if unique is 1
    if len(e1)==1 and len(e2)==1:
        count= abs(len(s11)-len(s22))
    else:
        if i in (s11,s22):
            count1= count1+s11.count(e1[i])
            print(count1)
            count2= count2+s22.count(e1[i])
            count=count1+count2
    print(count)    
    res= len(s1)+len(s2)+count
else:
    res= len(s1)+len(s2)
print(res)        
    
    
    
'''     if len(e1)==1 and len(e2)==1:
        count= abs(len(s11)-len(s22))
    else:
        if len(s11)>len(s22): # len(remaining chars) - len(unique chars)
            count= len(s11)-len(e1)
        else:
            count= len(s22)-len(e1)
        #print(count)
    res= len(s1)+len(s2)+count
else:
    res= len(s1)+len(s2)
print(res)'''

