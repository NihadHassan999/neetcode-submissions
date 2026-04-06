from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        count_s = Counter(list_s)
        count_t = Counter(list_t)
        if count_s == count_t:
            return True
        return False