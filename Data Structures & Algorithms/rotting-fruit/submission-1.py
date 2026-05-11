"""
multi source BFS
init queue, directions, rows, cols, fresh, time
collect all the 2 (rotting) oranges coordinates first into queue 
if fresh, then append to fresh variable
then do BFS of layer by layer rotting (appending to queue) and fresh count decrement
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # init queue, fresh, time, directions
        fresh = 0
        time = 0
        q = deque()

        # collection rotten and fresh into queue and fresh count
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        # do bfs
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            
            time += 1
        return time if fresh == 0 else -1

        

        