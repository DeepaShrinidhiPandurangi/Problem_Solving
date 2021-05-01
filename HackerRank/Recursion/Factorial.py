# Factorial

def factorial(n):
    if n == 1:
        return n # or 1
    else:
        return (n*factorial(n-1))

print(factorial(5))
''' Leave this in the same place as here in HackerRank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()