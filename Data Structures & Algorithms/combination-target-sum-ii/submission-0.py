'''
-> same approach of skipping duplicates by sorting and then comparing adjacent 
    elements to skip in while loop
-> create empty res and sort candidates
-> create dfs, success base case, i == len(candidates) return base case
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[::])
                return
            if total > target or i == len(candidates):
                return
            # append
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            # pop
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res 