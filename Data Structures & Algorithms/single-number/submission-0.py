'''
-> using XOR to find out the number which occurs only once
-> same numbers cancel out each other since x XOR x = 0
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res

'''
Time complexity : O(n) depends on the length of nums
Space complexity : O(1) no additional data structures are used
'''