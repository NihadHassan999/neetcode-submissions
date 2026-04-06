class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix # multiply prefix to res index
            prefix *= nums[i] # update prefix with current num index

        postfix = 1
        for i in range(len(nums) - 1, -1,-1):
            res[i] *= postfix # multiply prefix to res index
            postfix *= nums[i] # update prefix with current num index

        return res