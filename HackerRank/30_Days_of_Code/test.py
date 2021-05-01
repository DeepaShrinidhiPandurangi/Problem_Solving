t = int(input("enter the number of strings"))
for i in range(0,t):
    s1=""
    s2=""
    s = input("enter the strings")
    for i in range(0,len(s)):
        if i%2 == 0:
            s1= s1+s[i]
        else:
            s2= s2+s[i]
    print(s1," ",s2)