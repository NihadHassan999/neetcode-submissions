'''
-> initialise maxArea and stack (index, height) pair
-> iterate index and height 
-> if stack is not empty and curr element h < stack top element h, 
    then pop element from stack
-> calculate max area of popped index and height and set new index
-> iterate through remaining indexes and heights in stack to find again maxArea
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea