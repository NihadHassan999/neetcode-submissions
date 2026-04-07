from collections import Counter

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, init them
        l, r = 0, len(s)-1
        # while l<r, skip l and r alphanum
        while l<r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
        # check if not matching char
            if s[l].lower() != s[r].lower():
                return False
        # increment
            l += 1
            r -= 1
        return True