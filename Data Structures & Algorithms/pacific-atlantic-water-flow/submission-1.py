from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # init number of rows, number of cols, directions, ocean pac and alt
       # define bfs function where bfs(source, ocean)
       # create empty source pacific and atlantic and add the respective values to it
       # bfs on source
       # finally, create a res which has common values of both ocean pac and ocean alt
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]  
        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True                  
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        not ocean[nr][nc] and         
                        heights[nr][nc] >= heights[r][c]
                    ):
                        ocean[nr][nc] = True        
                        q.append((nr, nc))

        pacific = []
        atlantic = []
        for r in range(ROWS):
            pacific.append((r, 0))                  
            atlantic.append((r, COLS - 1))         

        for c in range(COLS):
            pacific.append((0, c))                
            atlantic.append((ROWS - 1, c))          

        bfs(pacific, pac)                        
        bfs(atlantic, atl)

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:        
                    result.append([r, c])
        return result                                 