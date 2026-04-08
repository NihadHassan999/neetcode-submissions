class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sum of l and r = target
        # l<r always
        # 1 indexed - we can use enumerate(numbers, start=1)
        # only one valid Solution
        # bigo1 space
        # TIP: 1 indexed can be done at end by adding 1 to the final returning indices
        # ---
        # init the pointers
        l, r = 0, len(numbers)-1
        # start the loop, while l<r, calculate and adjust pointers according to sum great or less
        while l<r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -=1 
            elif currSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []
