''' Day 5 : Tables : 1st 10 Multiples
Objective 
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.
Task 
Given an integer,n, print its first 10 multiples. Each multiple n*1  (where 1<=i<=10) should be printed on a new line in the form: n x i = result.
Input Format
A single integer,n.
Constraints
2<=n<=20
Output Format
Print 10 lines of output; each line i  (where 1<=i<=10) contains the  of n*1  in the form: 
n x i = result.
Sample Input
2
Sample Output
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20 '''

n= int(input("enter the number n \n"))
for i in range(1,11):  # If you don't give range, it will just compute for 1 and 11.
 multiple=n*i
 print(n ,"x",i,"=",multiple)
 
# Range manipulation  : range(arg1,arg2,arg3)  : range(start ,stop,step) 
# Print alternate multiples 
n1= int(input("enter the number n1 \n"))
for i in range(1,11,2):  # The third argument
 multiple1=n1*i
 print(n1 ,"x",i,"=",multiple1)
 
'''
output_combined

enter the number n
5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
enter the number n1
5
5 x 1 = 5
5 x 3 = 15
5 x 5 = 25
5 x 7 = 35
5 x 9 = 45 '''

# Tables in descending order
m= int(input("enter the number m \n"))
for i in range(10,0,-1):  # Step -1 for decreasing order
 multiple2=n1*i
 print(m ,"x",i,"=",multiple2)
'''
output

enter the number m
5
5 x 10 = 50
5 x 9 = 45
5 x 8 = 40
5 x 7 = 35
5 x 6 = 30
5 x 6 = 30
5 x 5 = 25
5 x 4 = 20
5 x 3 = 15
5 x 2 = 10
5 x 1 = 5  '''