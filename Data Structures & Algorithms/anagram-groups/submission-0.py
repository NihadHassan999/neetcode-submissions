'''

1) create a res hashmap defaultdict
2) in for each substring, create array of 26 characters
3) for each character, add count of charcter using ord
4) append the tuple converted array to whole res
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()