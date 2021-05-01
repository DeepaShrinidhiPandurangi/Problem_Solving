# Project Euler #1: Multiples of 3 and 5

################################################################################################
************Shortest Code :*********************************************************************
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    mult_3 = (n-1)//3
    mult_5 = (n-1)//5
    lcm = 3*5
    mult_35 = (n-1)//lcm
    sum_3 = 3*((mult_3*(mult_3+1))//2) 
    sum_5 = 5*((mult_5*(mult_5+1))//2)
    sum_15 = 15*((mult_35*(mult_35+1))//2)
# Note : division (x/y) and then converting to int() won't work in some versions of python for higher values. Use int div "//" as far as possible.
    sum =  sum_3 +sum_5 - sum_15
    print(sum)
************************************************************************************************
################################################################################################


# Old codes:
# Correct code
import time
t = int(input().strip())
for i in range(0,t):
    n = int(input().strip())
    #Check if the number is a multiple of 3 and append it to the lists of multiples of 3 and multiples of 5 respectively
    if (n -1)<3 :
        sum = 0
    elif (n-1) == 4:
        sum=3
    else:    
        q_3 = (n-1)//3
        q_5 = (n-1)//5
        q_15 = (n-1)//15
        sum_3=0
        sum_5=0
        sum_15=0
        if q_3 >0:
            sum_3 = 3*(q_3*(q_3 + 1))//2
        if q_5 >0:
            sum_5 = 5*(q_5*(q_5 + 1))//2
        if q_15 >0:
            sum_15 = 15*(q_15*(q_15 + 1))//2
        sum = sum_3+sum_5-sum_15
    print(sum)
    
    
# Time 
time_start = time.clock()
#run your code
time_elapsed = (time.clock() - time_start)
print(time_elapsed)


# My time consuming code
import time
t = int(input().strip())
print(t)
for a0 in range(t):
    n = int(input().strip())
    print(n)
    #Check if the number is a multiple of 3 and append it to the lists of multiples of 3 and multiples of 5 respectively
    multiples =[]
    for i in range(1,n):
        if i%3 == 0 or i%5 == 0:
            multiples.append(i)
    sum=0
    for i,j in enumerate(multiples):
        sum = sum + j
    print(sum)

    
# Time 
time_start = time.clock()
#run your code
time_elapsed = (time.clock() - time_start)
print(time_elapsed)


''' Second Method : Shri s time consuming code'''
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    #Check if the number is a multiple of 3 and append it to the lists of multiples of 3 and multiples of 5 respectively
    multiples_3 =[]
    multiples_5 =[]
    for i in range(1,n):
        if 3*i < n:
            multiples_3.append(3*i)
    for i in range(1,n):
        if 5*i < n:
            if 5*i not in multiples_3:
                multiples_5.append(5*i) 
    multiples = multiples_3+multiples_5            
    sum=0
    for i,j in enumerate(multiples):
        sum = sum + j
    print(sum)
    
# Time 
time_start = time.clock()
#run your code
time_elapsed = (time.clock() - time_start)
print(time_elapsed)
