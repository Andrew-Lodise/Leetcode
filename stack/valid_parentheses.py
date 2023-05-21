'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''
my thought is to have 3 variables keep track of each type of parentheses, starting at 0
make open parentheses of their type +1 and closing -1 

implemented that pretty easily, but I dont think it checks order

nope doesn't work need better alg
'''

'''
final solution: I used a dictionary to give chars within the same type of parentheses
the same value. My first check was to make sure the string has the same number of open and 
closed parentheses. Then loop throught the string and if its an open parenthese, append it 
to the stack, if its a close parentheses check if its the same type as the popped parenthese,
making sure the stack length isn't 0. 
'''

class Solution:
    # my solution. Time: O(n) Space: O(n)
    def isValid(self, s: str) -> bool:
        # dictionary with like parentheses having the same value to use later
        dict = {"(":0, ")":0, "[":1, "]":1, "{":2, "}":2}
        if len(s) % 2 == 1:
                return False
        # first checking to see if they are the same number of open and closed parentheses
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        open_count = 0
        close_count = 0
        for c in s:
            if c in open:
                open_count += 1
            
            if c in close:
                close_count += 1

        if open_count != close_count:
            return False
        # looping through, open paren = append, close paren = pop and compare
        stack = []
        for c in s:
            if c in ["(","[","{"]:
                stack.append(c)
            
            if c in [")","]","}"]:
                if len(stack) == 0:
                    return False
                
                if dict[c] != dict[stack.pop()]:
                    return False
            
        return True
    
    #neetcodes solution, very similar, little more concise, same time and space
    def isValid2(self, s: str) -> bool:
        stack = []
        close_to_open = {")":"(", "]":"[", "}": "{"}

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return True if not stack else False
    
mysol = Solution()
print(mysol.isValid2("){"))

#scrap notes
# a = '()'
# b = '{}'
# c = '[]'

dict = {"(":0,
        ")":0,
        "[":1,
        "]":1,
        "{":2,
        "}":2,}

s = "(]"
stack = []
for c in s:
    #print("---------")
    #print("c =",c)

    if c in ["(","[","{"]:
        stack.append(c)

    #print("stack =", stack)
    
    if c in [")","]","}"]:
        #print(dict[c] == dict[stack.pop()])
        pass
    
