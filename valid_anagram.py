'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.
'''
# making hashmaps with the frequencies again idk what else to do
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

        
mysol = Solution()
print(mysol.isAnagram("andrew", "werdna" ))


# notes
str = "andrew"
str2 = "werand"
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

