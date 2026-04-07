class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # init longest
        longest = 0
        num_set = set(nums)
        # start and assign curr and length if previous does not exist
        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                length = 1
        # if next exists, increment both curr and length
                while curr + 1 in num_set:
                    curr += 1
                    length += 1
        # get max of length and longest 
                longest = max(longest, length) 
        
        return longest