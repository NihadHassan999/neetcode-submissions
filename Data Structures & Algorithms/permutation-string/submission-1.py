'''
-> check lengths of s1 and s2 and compare check
-> sort s1
-> iterate through all windows in s2 with size of s1
-> sort the current window and compare it with s1
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        sorted_s1 = sorted(s1)

        for i in range(len_s2 - len_s1 + 1):
            current_window = s2[i:i + len_s1]
            if sorted(current_window) == sorted_s1:
                return True
        return False
