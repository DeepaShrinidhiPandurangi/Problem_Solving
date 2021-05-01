# To check if the given number is perfect square:

def is_square(n):
    import math
    if n < 0:
        return False
    else:
        if math.sqrt(n)%1 ==0:
            return True
        else:
            return False
