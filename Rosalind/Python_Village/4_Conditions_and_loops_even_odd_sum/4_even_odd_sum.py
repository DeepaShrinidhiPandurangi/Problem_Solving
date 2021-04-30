#Good example to learn how to use while and for loops
# Method 1
a= int(input("enter the num a :\n"))
b= int(input("enter the num b :\n"))

evensum=0
oddsum=0
for i in range(a,b+1):  #################### Note : while i<=b and i>=a with i=0  is wrong. The initial value of i changes with while loop.  
 if i%2==1:
  oddsum=oddsum+i
 elif i%2==0:
  evensum=evensum+i
print("oddsum:",oddsum,"evensum:",evensum)

''' eg.o/p : for 1,10 = oddsum: 25 evensum: 30'''

# While loop
# Method 2
# If you want to use while loop, do not initialize i to 0. Initialize it to a . As there are 2 conditions.
# i is a counter here. You have to initialize it to a for it to iterate till b . It cannot use range like for loop.
# While loop depends on conditions true and false . For loop depends on the condition it has to iterate.
a= int(input("enter the num a :\n"))
b= int(input("enter the num b :\n"))

evensum=0
oddsum=0
i=a
while i>=a and i<=b: # while can be used like for loop to set range . take care about the initialization of "i".
 if i%2==1:
  oddsum=oddsum+i
 elif i%2==0:
  evensum=evensum+i
 i=i+1
print("oddsum:",oddsum,"evensum:",evensum)

# For loop
# Method 3
# Sum of all , odd and even integers between 2 numbers,inclusively
a = 1
b = 10
sum1 = 0 # do not use sum as sum is an inbuilt function
sum2 = 0
sum3 = 0
for i in range(a,b+1):
  sum1 = sum1+ i
  #print(i)
  if i%2 == 0:
    sum3 = sum3+ i
    #print(i)
print("the sum of all the numbers is:\n",sum1)
print("the sum of all even numbers is:\n",sum3)

# Method 4 - most simple
for i in range(a,b+1,2):
  sum2 = sum2+ i
  #print(i)
print("the sum of all odd numbers is:\n",sum2)

'''
the sum of all the numbers is:
 55
the sum of all even numbers is:
 30
the sum of all odd numbers is:
 25
 '''