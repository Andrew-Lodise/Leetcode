'''
This is a second attemp at this problem because I want to understand it better
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize pointers and max profit
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            #check to see if we have a profit, set new max profit if it is
            cur_profit = prices[r] - prices[l]
            max_profit = max(max_profit, cur_profit)

            # print statement to see everything
            #print("l =",l,"\tr =",r,"p[l] =", prices[l], "p[r] = ", prices[r], "maxp =", max_profit)

            #check to see if right is less than left, set left pointer = right pointer if it is
            if prices[l] > prices[r]:
                l = r
            
            r+=1
        
        return max_profit

mysol = Solution()
print(mysol.maxProfit([7,6,4,3,1]))

# scrap notes

prices = [7,1,5,3,6,4]
l, r = 0, 1
max_profit = 0
while r < len(prices):

    #check to see if we have a profit, set new max profit if it is
    cur_profit = prices[r] - prices[l]
    max_profit = max(max_profit, cur_profit)

    # print statement to see everything
    #print("l =",l,"\tr =",r,"p[l] =", prices[l], "p[r] = ", prices[r], "maxp =", max_profit)

    #check to see if right is less than left, set left pointer = right pointer if it is
    if prices[l] > prices[r]:
        l = r
    
    r+=1

