'''
A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
'''

'''
So first I have to remove all non-alphanumeric characters and 
convert all letters to lowercase, next I have to start with the first and last
letters in the string and make sure they are equal, and move inward with both 
after each test
'''


class Solution:
    # my solution using a list and for loops | Time: O(2n/2) Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        # Makes a list with only lowercase alphanumeric chars
        r = []
        for c in s:
            if c.isalpha() or c.isdigit():
                r.append(c.lower())

        for i in range(round(len(r)/2)): 
            if r[i] != r[(-1*i)-1]: 
                return False
            
        return True
    
    # neetcode solution | Time: O(n) Space: 0(n)
    def isPalindrome2(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]
    
    # neetcode solution 2 | Time: O(n) Space: O(1)
    def isPalindrome3(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1

        return True
    
    # leetcode solution using list comprehension | Space: O(n) Time: O(n)
    def isPalindrome4(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return (s == s[::-1])
        
mysol = Solution()
print(mysol.isPalindrome3("0PP"))

# scrap notes

s = "And8D n A!"

#.lower() converts to lowercase
#.isalpha() returns True if its a character
#.isdigit() return True if its a number
r = []
for c in s:
    if c.isalpha() or c.isdigit():
        r.append(c.lower())

#print(r)

# ^ this removes the non-alphanumeric characters

# if the word has an odd amount of letters I need to go n//2 + 1
# and if it has even letters I just have to go n/2

for i in range(round(len(r)/2)): # I goes 0, 1 ,2 but I want to compare r[0] to r[-1]
    if r[i] != r[(-1*i)-1]: # looks weird but it's the right comparisons
        pass #print(False)
    
    #print(True)
