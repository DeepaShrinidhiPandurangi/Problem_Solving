import math
a= float(input ("The side a of the triangle is : "))
b= float(input ("The side b of the triangle is : "))
d= ((a**2)+(b**2))
c= math.sqrt(d)
if a!=0 and b!=0 :
 print ("The side c of the triangle is", c)
else :
  print ("Error: The sides a and b of the triangle have to be greater than 0")