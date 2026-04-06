'''
-> create empty maxp and pointer values should point to 0 and 1 index
-> through length of list, if current buy price<next price, then obtain maxP 
-> else, next price becomes current buy price
-> finally finish the loop by incrementing for next iteration
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP