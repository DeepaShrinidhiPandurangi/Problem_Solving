a = input("Enter the DNA \n")
r= a[::-1]#Reverse the string
replacedString = ''
#Complement it
for i in r:
 if i == 'A':
  replacedString += 'T'  # += adds another value with the variable's value and assigns the new value to the variable.
 elif i == 'T':
  replacedString += 'A'
 elif i == 'G':
  replacedString += 'C'
 else:
  replacedString += 'G'
print ("\n", replacedString)
# += adds another value with the variable's value and assigns the new value to the variable.



#or
s= "AAAACCCGGT"
s=s[::-1]
res =""
for i in s:
  if i == "T":
    res= res+"A"
  elif i == "G":
    res = res+"C"
  elif i == "C":
    res =res+ "G"
  elif i == "A":
    res = res+"T"
print(res)

# Reverse without using short-cut
s= "AAAACCCGGT"
s1 = ""
for i in range(len(s)-1,0,-1):
  s1= s1+s[i]
print(s1)


# clever online code
st = "AAAACCCGGT"
st = st.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()[::-1]
print(st)
