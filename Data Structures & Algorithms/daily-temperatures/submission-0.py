'''
-> create res with 0 default for len(temperatures) and stack
-> enumerate through temperatures
-> if stack is not empty and curr temp > highest temp in stack, then pop the current temp and index 
-> get the difference of index and add to res
-> if not, append curr temp and index to stack
-> return res
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))
        return res

'''
Time complexity : O(n)
Space complexity : O(n)
'''