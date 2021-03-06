# Two Sum
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


'''
Approach 1: Brute Force
The brute force approach is simple. Loop through each element xx and find if there is another value that equals to target - xtarget−x.
'''
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(0,len(nums)):
		    L1=[]
		    for j in range(i+1,len(nums)):
		      if (nums[i]+nums[j]) == target:
		                L1.append(i)
		                L1.append(j)
		                return(L1)
		                break
'''
The brute force approach is simple. Loop through each element x and find if there is another value that equals to target (target−x)

Complexity Analysis

Time complexity : O(n^2)
For each element, we try to find its complement by looping through the rest of array which takes O(n)O(n) time. Therefore, the time complexity is O(n^2).

Space complexity : O(1)
'''


'''
Approach 2: Two-pass Hash Table
To improve our run time complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to look up its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.

We reduce the look up time from O(n)O(n) to O(1)O(1) by trading space for speed. A hash table is built exactly for this purpose, it supports fast look up in near constant time. I say "near" because if a collision occurred, a look up could degenerate to O(n)O(n) time. But look up in hash table should be amortized O(1)O(1) time as long as the hash function was chosen carefully.

A simple implementation uses two iterations. In the first iteration, we add each element's value and its index to the table. Then, in the second iteration we check if each element's complement (target - nums[i]target−nums[i]) exists in the table. Beware that the complement must not be nums[i]nums[i] itself!
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        L=[]
        for i in range(0,len(nums)):
          complement = target-nums[i] 
          if complement in D:
            L.append(D[complement]) # return [D[complement],i],instead of this and next 2 lines.
            L.append(i)
            return (L)
          D[nums[i]]=i
'''
Complexity Analysis:

Time complexity : O(n). We traverse the list containing nn elements exactly twice. Since the hash table reduces the look up time to O(1), the time complexity is O(n).

Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly nn elements.'''




'''Runtime calculation:

import timeit
def twoSum(nums,target):
  start = timeit.default_timer()
  for i in range(0,len(nums)):
      L1=[]
      for j in range(i+1,len(nums)):
        if (nums[i]+nums[j]) == target:
                  L1.append(i)
                  L1.append(j)
                  print(L1)
                  break
  stop = timeit.default_timer()

  print('Time: ', stop - start) 
print(twoSum([3,4,5,3,6],6))

import timeit
def twoSum(nums,target):
    start = timeit.default_timer()
    D = {}
    L=[]
    for i in range(0,len(nums)):
      complement = target-nums[i] 
      if complement in D:
        L.append(D[complement])
        L.append(i)
        print (L)
      D[nums[i]]=i
    stop = timeit.default_timer()

    print('Time: ', stop - start) 
print(twoSum([3,4,5,3,6],6))
'''
