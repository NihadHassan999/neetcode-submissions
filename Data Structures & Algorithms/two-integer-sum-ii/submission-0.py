#1) use two pointers to traverse (sorted is advantage)
#2) find curr sum using curr pointers
#3) if currsum is less than target, left pointer increment
#4) if currsum is greater than target, right pointer decrement

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum < target:
                l += 1

            elif currSum > target:
                r -= 1
            
            else:
                return [l + 1, r + 1]
            
        return []