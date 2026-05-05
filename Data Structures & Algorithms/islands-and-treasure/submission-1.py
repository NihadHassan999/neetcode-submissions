from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
       # init everything queue, inf, directions, visited, rows, cols
       # get all the 0s , mark visited and append to queue  
       # then traverse the queue and for each nr nc , if the checks pass -> mark visited, update dist and append to queue
       rows, cols = len(grid), len(grid[0])
       INF = 2147483647
       q = deque()
       visited = set()

       for r in range(rows):
        for c in range(cols):
            if grid[r][c]==0:
                q.append((r,c))
                visited.add((r,c))

       while q:
        r,c = q.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = dr + r, dc + c
            if (0 <= nr < rows and 0 <= nc < cols
                and (nr, nc) not in visited
                and grid[nr][nc] != -1):
                visited.add((nr,nc))
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))