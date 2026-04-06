
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = {}

        for word in strs:
            str_list = list(word)
            str_list.sort()
            key = "".join(str_list)
            if key not in visited:
                visited[key] = [word]
            else:
                visited[key].append(word)
        
        return list(visited.values())