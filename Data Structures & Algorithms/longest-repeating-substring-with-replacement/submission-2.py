'''
-> create hashset and res with l = 0
-> iterate indices through len(s) and add count and find maxf
-> if length - maxf > k, then remove current first pointer value from count and increment first pointer position
-> finally return substring length
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
        