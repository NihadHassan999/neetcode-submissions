"""
-> here its max(), make decision of max(skip, rob)
-> use 2 as starting because prev and curr is already 0 and 1
-> also we need to consider adjacent houses constraint
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(curr, prev + nums[i])
            prev = curr
            curr = temp
        
        return curr

"""
time : O(n) -> need to look each house atleast once
space : O(1) -> just few variables
"""