class Solution:
    def isValid(self, s: str) -> bool:
        '''
        first set up a dictionary so that each open
        paren is matched with its corresponding closed
        paren
        '''
        parens = {"(":")",
                  "[":"]",
                  "{":"}"}
        
        #set up a stack
        stack = []

        for c in s:
            if c in parens: # open parens
                stack.append(c) 

            '''
            for closing parens ..
            check if stack isn't empty already
            and check if the closing paren is the same
            as the last open paren on the stack
            if it is we pop that off the stack
            otherwise we know its invalid.
            '''
            if c not in parens: 
                if stack and (parens[stack[-1]]) == c:
                    stack.pop()
                else:
                    return False
                
        if not stack: # if stack ends up being empty
            return True
        else:
            return False
