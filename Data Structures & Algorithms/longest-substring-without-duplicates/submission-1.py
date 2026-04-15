class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      # input: zsyzsyz
      # output: 3
      charset = set()
      l = 0
      res = 0
      n = len(s)

      for r in range(n):
        while s[r] in charset:
            charset.remove(s[l])
            l += 1
        # expand
        charset.add(s[r])

        # update final result
        res = max(res, r - l + 1)

      return res

      
