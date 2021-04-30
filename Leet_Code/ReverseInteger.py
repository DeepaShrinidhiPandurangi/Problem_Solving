7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x< 0 :
            rev = -int(str(x)[1:][::-1])
            if rev > -2**31:
                return (rev)
            else:
                return 0
        else:
            rev = int(str(x)[::-1])
            if rev < (2**31)-1:
                return (rev)
            else:
                return 0  
print(reverse(-132))
print(reverse(1534236469))
print(reverse(1463847412))
				
				
				
				
'''Other language approaches :
https://leetcode.com/problems/reverse-integer/solution/

Approach 1: Pop and Push Digits & Check before Overflow
Intuition

We can build up the reverse integer one digit at a time. While doing so, we can check beforehand whether or not appending another digit would cause overflow.

Algorithm

Reversing an integer can be done similarly to reversing a string.

We want to repeatedly "pop" the last digit off of xx and "push" it to the back of the \text{rev}rev. In the end, \text{rev}rev will be the reverse of the xx.

To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.

//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;
However, this approach is dangerous, because the statement \text{temp} = \text{rev} \cdot 10 + \text{pop}temp=rev⋅10+pop can cause overflow.

'''
#python 3 solution internet
class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        if x > 0:
            s = x
        else:
            s = -1 * x
        while (s != 0): 
            last = s % 10
            s = int (s /10)
            reverse = reverse * 10 + last
        if reverse > 2 ** 31 - 1:
            return 0
        if x < 0: 
            return -1 * reverse
        return reverse 