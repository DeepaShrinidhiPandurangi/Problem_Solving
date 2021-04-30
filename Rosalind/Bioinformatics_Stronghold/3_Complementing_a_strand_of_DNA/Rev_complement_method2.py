str_a= input("enter the DNA string \n")
str_rev = str_a[::-1]
print('reverse_string is:\n',str_rev)
index = 0
print('reverse_complement is:')
while index < len(str_rev):
     letter = str_rev[index]
     if letter == 'A':
        print('T'),end='')
     elif letter == 'T':
        print('A'),end='')
     elif letter == 'C':
        print('G'),end='')
     else:
        print('C'),end='')
     index = index + 1


# or
s= "AAAACCCGGT"
s=s[::-1] # Reverse without using short-cut written below
res =""
for i in range(0,len(s)): 
  if s[i] == "T":
    res= res+"A"
  elif s[i] == "G":
    res = res+"C"
  elif s[i] == "C":
    res =res+ "G"
  elif s[i] == "A":
    res = res+"T"
print(res)

# Reverse without using short-cut
s= "AAAACCCGGT"
s1 = ""
for i in range(len(s)-1,0,-1):
  s1= s1+s[i]
print(s1)