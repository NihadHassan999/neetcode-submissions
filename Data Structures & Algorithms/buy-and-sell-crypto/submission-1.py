class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # calculate profit and increase based on max(result, profit)
       # init pointers and max profit
       # when r< length of prices list, if price r > price l -> calculate max profit and max()
       # else we can +1 the buy pointer to get a lower buy price
        l, r = 0, 1 
        maxP = 0

        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP