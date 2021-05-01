# Convert input with spaces on a single line to elements in a list
i= list(map(int,input("enter the numbers with a space in between on a single line ").split( )))
print(i)

# o/p: enter the numbers with a space in between on a single line 1 2 3 4 5
# [1, 2, 3, 4, 5]