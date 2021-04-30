'''Max Consecutive Ones

Solution
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000nums=[1,1,0,1,1,1]
'''

def findMaxConsecutiveOnes(nums):
  s = ""
  for i in range(0,len(nums)):
    s= s+str(nums[i])
    L = s.split("0")
  return len(max(L))

print(findMaxConsecutiveOnes(nums))

#Time : 7092 ms


#On leet code website: 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = ""
        for i in range(0,len(nums)):
            s= s+str(nums[i])
            L = s.split("0")
        return len(max(L))


# More faster solution:
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count= 0
        L=[]
        for i in nums:      # or  for i in range(0,len(nums)):
            if i == 1:      # nums[i] == 1
                count+= 1
            else:
                L.append(count)
                count = 0
        return max(L)
#Time : 368 ms                #384 ms


# Internet : see how to create temp variable to compare previous and current values

def f1(nums):
  cnt, res = 0,0
  for n in nums:
    cnt = cnt + 1 if n == 1 else 0
    res = max(res, cnt)  # Note: res = max(res,cnt) = using res on both sides to store previous values and replace the value only if the new value is higher.
  return res

print(f1(nums))


#or 
s= "110011100001111000001101000001111110001001"
temp=0
count=0
L=[]
for i in range(0,len(s)):
  if s[i]== "1":
    count+=1
    temp=count
  else:
    count=0
  L.append(max(temp,count))
print(max(L))
