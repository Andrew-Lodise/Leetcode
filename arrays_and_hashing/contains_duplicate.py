from typing import List

"""
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""


class Solution:
    # My solution | Time: O(n^2) Space: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set a hash map to the occurances of each number
        dict = {}
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
            # use the any function to see if any occurances are more than one
            return any(n > 1 for n in dict.values())
        
    # Time: O(n) Space: O(n)
    def containsDuplicate2(self, nums: List[int]) -> bool:
        # better than previous because it doesn't need to count at the end
        dict = {}
        for n in nums:
            if n not in dict:
                dict[n] = 1
            else:
                return True
        return False
    
    # neetcode answer using a set/hashset | Time: O(n) Space: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    # one liner useing a set and comparison in size    
    def containsDuplicate3(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)




mysolution = Solution()
print(mysolution.containsDuplicate2([1, 2, 3, 4, 5]))
