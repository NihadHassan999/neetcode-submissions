from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        freq_s = Counter(s_list)
        freq_t = Counter(t_list)
        if freq_s == freq_t:
            return True
        return False