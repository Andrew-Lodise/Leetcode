from typing import List

'''
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      dict = {}
      for n in nums:
        if n not in dict:
          dict[n] = 1
        else:
          dict[n] += 1

      return (any(n>1 for n in dict.values()))
    

mysolution = Solution()
print(mysolution.containsDuplicate([1,2,3,4,5,5]))