'''
-> create empty res 
-> sort if not sorted
-> create backtrack function
-> edgecase : if i reached len(nums), then we reached end of subset, append the subset
-> add next i, backtrack, pop
-> edge case to skip duplicates , backtrack
-> finally call the backtrack and return res
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort if not sorted already
        nums.sort()

        def backtrack(i, subset):
            # if index exceeds nums, then append the subset and return res
            if i == len(nums):
                res.append(subset[::])
                return 
            
            # add and backtrack, pop
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # skip duplicates edge cases by incrementing
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        # finally call the backtrack function and return res
        backtrack(0, [])
        return res