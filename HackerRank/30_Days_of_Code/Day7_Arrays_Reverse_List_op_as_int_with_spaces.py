'''Day 7: Arrays : Reverse a list (given as integers separated by spaces'''

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
#My code line added
print(*arr[::-1]) #print(*a) = converts list to integers with spaces. This trick uses unpacking to pass the list items to 
                  #print as separate arguments, so that they get separated by spaces.
                  
'''
The rstrip() removes characters from the right based on the argument (a string specifying the set of characters to be removed).

The syntax of rstrip() is:string.rstrip([chars])
rstrip() Parameters - Takes one argument
chars (optional) - a string specifying the set of characters to be removed.
If the chars argument is not provided, all whitspaces on the right are removed from the string.'''

'''
split() method returns a list of strings after breaking the given string by the specified separator.

Syntax :

str.split(separator, maxsplit)
Parameters :  Takes 2 arguments

separator : The is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.

maxsplit : It is a number, which tells us to split the string into maximum of provided number of times. If it is not provided then there is no limit.
'''