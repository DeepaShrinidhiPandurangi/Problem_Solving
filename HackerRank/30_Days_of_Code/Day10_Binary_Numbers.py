#if __name__ == '__main__':
    n = int(input())
    b = bin(n)
    b = b[2:]
    L= [0]
    #print(b)
    b = b.split("0")
    #print(b)
    print(len(max(b , key =len)))
