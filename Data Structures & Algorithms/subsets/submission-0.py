'''
-> create res and subset list
-> create dfs function inside existing subsets function
-> base case : return solution if index exceeds len(nums)
-> add one : dfs, subtract one : dfs
-> now outside function, dfs(0)
-> return res
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res