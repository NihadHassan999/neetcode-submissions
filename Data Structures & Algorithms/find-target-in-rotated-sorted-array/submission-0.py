'''
-> l, r is initialised
-> since its sorted at a pivot point, we need to check through both left and right sorted halves
-> find mid, if mid == target, then return mid 
-> if l pointer value <= mid value, its left sorted and check there
-> else, its right shorted and check there
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid =(l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1