# 1st method

a = input("Enter the DNA : \n")
b = len(a)
# C= str(a) ..ensuring the value is read as a string
CountA = 0
CountT= 0
CountG = 0
CountC = 0

for i in a:
 if i == 'A':
  CountA = CountA +1

 if i == 'T':
  CountT = CountT +1

 if i == 'G':
  CountG = CountG +1

 if i == 'C':
  CountC += 1
  # Alternate way of iterating the counter

print ("\n The length of the DNA is :",b)
print ("\n The number of A,T,G,C in the given DNA are :" , CountA ,CountT ,CountG ,CountC ,"respectively") 

################################## You can do this in one line.
s=input("Input your string:")
print(*(s.count("A"),s.count("C"),s.count("G"),s.count("T")))# "*" unpacks the output and passes it as separate entities


