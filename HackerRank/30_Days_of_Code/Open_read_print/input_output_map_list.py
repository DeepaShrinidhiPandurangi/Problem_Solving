# Convert the input of single elements in a line in command line to a list in the program

# I = list(map(str,input("enter the words in a line separated by space (add "" as they are strings) \n").split()))
# S = list(map(int,input("enter the numbers(int) in a line separated by space \n").split()))
# F = list(map(float,input("enter the numbers(decimals/int) \n").split()))
# print(I)
# print(S)
# print(F)
'''
o/p:
enter the words in a line separated by space (add  as they are strings)
"hello" "world" "How are you ?"
enter the numbers(int) in a line separated by space
1 2 3 4 5 1001
enter the numbers(decimals/int)
0.1 0.28734 0.789 67.90
['"hello"', '"world"', '"How', 'are', 'you', '?"']
[1, 2, 3, 4, 5, 1001]
[0.1, 0.28734, 0.789, 67.9]
'''

# Convert list items to individual values in output separated by spaces
L1 = [1, 2, 3, 4, 5, 1001]
L2 = ['"hello"', '"world"', '"How', 'are', 'you', '?"']
L3 = [0.1, 0.28734, 0.789, 67.9]
print(*L1[::])
print(*L2[::])
print(*L3[::])
# Reverse
print(*L1[::-1])
print(*L2[::-1])
print(*L3[::-1])


'''o/p :
1 2 3 4 5 1001
"hello" "world" "How are you ?"
0.1 0.28734 0.789 67.9 

1001 5 4 3 2 1
?" you are "How "world" "hello"
67.9 0.789 0.28734 0.1
'''