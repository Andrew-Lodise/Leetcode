'''
You are given an array prices where prices[i] is
the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to
buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not
allowed because you must buy before you sell.
'''

'''
my thought it to just find the minimum of the list, then find the max
of the sublist starting at the min but that might not work lets try
'''

'''
my first attempt did not work, so I'm just going to use brute force

I think I was thinking about this all wrong I'll give it another 30 min before I give up
ok my new way is kinda working
'''

from typing import List


class Solution:
    # my first failed solution
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        minnimum = min(prices)
        if prices.index(minnimum) == len(prices) - 1:
            minnimum = min(prices[:-1])
        ps = prices[prices.index(minnimum):]
        maximum = max(ps)
        profit = maximum - minnimum
        return profit
    
    # my second solution using brute force
    def maxProfit2(self, prices: List[int]) -> int:
        # trying to minimize the time it takes
        if p == sorted(p, reverse=True):
            return 0

        profit = 0
        for i, n1 in enumerate(prices):
            #print(n1, p[i+1:])
            for n2 in prices[i+1:]:
                if (n2 - n1) > profit:
                    profit = n2 - n1

        return profit
    
    # third solution unlucky doesn't work still a good try
    def maxProfit3(self, prices: List[int]) -> int:
        #set the left = first and right = last
        l = prices[0]
        r = prices[-1]

        # move left if its smaller, move right if its bigger, stop if indices match
        while (prices.index(l) != prices.index(r) and
               prices[prices.index(l)+1] < l):
            l = prices[prices.index(l)+1]

        while (prices.index(l) != prices.index(r) and
               prices[prices.index(r)-1] > r):
            r = prices[prices.index(r)-1]

        return r - l
    
    #neetcodes solution
    def maxProfit4(self, prices: List[int]) -> int:
        l,r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r+=1
        
        return max_profit




    
mysol = Solution()
print(mysol.maxProfit4([7,1,5,3,6,4]))
    
# scrap notes

p = [5,4,3,2,1]#[7,5,1,3,6,4] 
#min = min(p)
#print(min)
#print(p.index(min))
#print(ps)
##profit = max - min
#print(profit)

profit = 0
for i, n1 in enumerate(p):
    #print(n1, p[i+1:])
    for n2 in p[i+1:]:
        if (n2 - n1) > profit:
            profit = n2 - n1

#print(profit)
#print(p == sorted(p, reverse=True))

prices = [7,1,5,3,6,4]#[2,4,1]
#prices = sorted(prices, reverse=True)
#print(prices)
# what if I set the left = first and right = last
l = prices[0]
r = prices[-1]
#print(l,r)
# move left to the right if its smaller, move right to the left if its bigger
while (prices.index(l) != prices.index(r) and
       prices[prices.index(l)+1] < l):
    l = prices[prices.index(l)+1]
    #print("l=",l)

while (prices.index(l) != prices.index(r) and
       prices[prices.index(r)-1] > r):
    r = prices[prices.index(r)-1]
    #print("r=",r)

#print(l, r,r-l)