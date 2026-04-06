'''
-> initialise res, l, r
-> start binary search
-> if number at l index < number at r index, get min res
    and break
-> get middle, get min res of that
-> then do if middle value >= l value, go to right else left
-> return res
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

'''
Time complexity : O(logn)
Space complexity : O(1)
'''
        