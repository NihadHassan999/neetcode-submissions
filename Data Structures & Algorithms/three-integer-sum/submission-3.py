class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       # input = [-1,0,1,2,-1,-4]
       # output = [[-1,-1,2],[-1,0,1]]
       #-----
       # sort the numbers and init res
       nums.sort()
       res = []
       # start loop, duplicates check
       for i in range(len(nums)):
        if i>0 and nums[i] == nums[i-1]:
            continue
       # set two pointers
        l, r = i + 1, len(nums) - 1
       # start two pointers, calculate total
        while l<r:
            total = nums[i] + nums[l] + nums[r]
       # usual two pointer stuff, < total > total
            if total > 0:
                r -= 1
            elif total < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l<r and nums[l] == nums[l+1]:
                    l += 1
                while l<r and nums[r] == nums[r-1]:
                    r -= 1
       # else append to res list and update pointers along with duplicate check
                l += 1
                r -= 1
        
       return res