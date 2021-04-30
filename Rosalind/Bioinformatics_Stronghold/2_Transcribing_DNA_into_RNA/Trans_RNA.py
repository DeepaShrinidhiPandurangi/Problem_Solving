u= input("Enter the DNA string \n")
t = u.replace("T","U",1000)
print("The total length of the transcribed RNA string is ",len(t))
print("The transcribed RNA is ",t)
#print("The transcribed RNA is ",t[0:1000]) if you want to limit the output length
