class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = width * height, so its (r-l)* min(l or r height)
        # the idea is to keep increasing the lower height always
        res = 0
        l, r = 0, len(heights) - 1

        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res 