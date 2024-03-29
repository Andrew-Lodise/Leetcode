''' Question
Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order.
'''

from typing import List


class Solution:
    # my solution using two loops | Time complexity: O(n^2) Space Complexity O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and nums[i] + nums[j] == target:
                    return [i, j]
    
    # neetcode solution using a hashmap | Time complexity: O(n) Space complexity: O(n)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, n in enumerate(nums):
            remaining = (target - n)
            if remaining in dict:
                return [i, dict[remaining]]
            
            dict[n] = i     # stores numbers as number : index
    

#test    
mysol = Solution()
print(mysol.twoSum2([3,3], 6))