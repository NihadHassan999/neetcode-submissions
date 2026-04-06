"""
1 step 1 way, 2 step 2 ways
after that loop and keep considering latest 2 elements
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (1,2):
            return n
        first=1
        second=2
        for i in range(3, n+1):
            current = first + second
            first = second
            second = current
        return second

"""
time complexity : here the for loop increase with n, so O(n)
space complexity : few variables being used, so O(1)
"""