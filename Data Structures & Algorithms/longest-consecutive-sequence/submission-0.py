# create hashset and initialiase result(longest)
# iterate, if left neighbour not present, it starts a new sequence = 1
# if next neighbour (current + length) is present, increment legnth
# finall find longest by max and return it 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
            