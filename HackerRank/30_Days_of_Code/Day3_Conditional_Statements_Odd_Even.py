'''Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 , print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird'''


n=int(input("enter a number:"))

if n %2 != 0:
  print("Weird")

else:
  if n%2 ==0:
    if n in range(2,6):   # while using range , use (x,y+1).Here 5 becomes 6 as range excludes the 2nd value 
      print("Not Weird")
    
    elif n in range(6,21):
      print("Weird")
  
    elif n>20 :
      print("Not Weird")