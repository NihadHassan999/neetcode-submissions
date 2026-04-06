'''
-> list could be [1, 100, 2] -> 0th step cost is 1, 1st step cost is 10, like that
-> formula would be min cost of jumping from current step + min(i+1 step cost + i+2 step cost)
-> edge cases to be considered first -> array length exceed, checking memo
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def minCost(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(minCost(i+1), minCost(i+2))
            return memo[i]
        return min(minCost(0), minCost(1))