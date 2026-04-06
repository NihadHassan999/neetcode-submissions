'''
-> initialize empty set and res
-> define two pointers for sliding window, 0 and 1
-> if second pointer value in set, remove the first pointer value, increment it and add the new one
-> 
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        