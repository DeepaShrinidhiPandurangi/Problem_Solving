'''Day 1.Data Types
Declare  variables: one of type int, one of type double, and one of type String.
Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your variables.
Use the  operator to perform the following operations: 
Print the sum of  plus your int variable on a new line.
Print the sum of  plus your double variable to a scale of one decimal place on a new line.
Concatenate  with the string you read as input and print the result on a new line.

Input Format

The first line contains an integer that you must sum with . 
The second line contains a double that you must sum with . 
The third line contains a string that you must concatenate with .

Output Format

Print the sum of both integers on the first line, the sum of both doubles (scaled to  decimal place) on the second line, and then the two concatenated strings on the third line.'''
i = 4
d = 4.0
s = 'HackerRank '

i1 = int(input("i1 is:"))
d1= float(input("d1 is:"))
s1= str(input("s1 is:"))
print(i+i1)
print(d+d1)
print(s+s1)

'''Test Cases
Compiler Message
Success

1.
Input (stdin)
4.0
is the best place to learn and practice coding!
Expected Output
16
8.0
HackerRank is the best place to learn and practice coding!

2.
Input (stdin)
3
2.8
is my favorite platform!

Expected Output
7
6.8
HackerRank is my favorite platform!'''
