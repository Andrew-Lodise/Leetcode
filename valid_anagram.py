'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.
'''
# my solution using two hashmaps | Time: O(s + t) Space: O(s + t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for letter in s:
            if letter not in hashmap1:
                hashmap1[letter] = 1
            else:
                hashmap1[letter] += 1

        for letter in t:
            if letter not in hashmap2:
                hashmap2[letter] = 1
            else:
                hashmap2[letter] += 1

        return hashmap1 == hashmap2
    
    
    # Solution using count method on strings which I did not know about 
    def isAnagram2(self, s, t):

        if len(s) != len(t):
            return False
        
        for idx in set(s):
            if s.count(idx) != t.count(idx):
                return False
            
        return True   

    # leetcode solution, pretty similar to mine actually
    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT  

        
mysol = Solution()
#print(mysol.isAnagram("andrew", "werdna" ))


# scrap notes
str = "andrew"
str2 = "werand"

print(str.count("a"))
print("anagram".count("a"))

hashmap = {}
for letter in str:
    if letter not in hashmap:
        hashmap[letter] = 1
    else:
        hashmap[letter] += 1

hashmap2 = {}
for letter in str2:
    if letter not in hashmap2:
        hashmap2[letter] = 1
    else:
        hashmap2[letter] += 1

#for letter in hashmap:
    #if letter not in hashmap2:
        #print("false")

    #print(hashmap[letter] == hashmap2[letter])

#print(hashmap)
#print(hashmap2)
#print(hashmap == hashmap2)

# takeaways
"""
with strings you can use a .count(letter) to check how many occurances
ex: "anagram".count("a") = 3 

finding a fast way to disprove something can speed up runtime quickly 
like checking if the two strings are not the same length
"""
