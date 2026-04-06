'''
-> define queue, fresh, time
-> get fresh count, rotten goes to queue
-> define directions, while fresh or q exists : do bfs in all directions from queue
-> return time
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        # take count of fresh and rotten oranges
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        # bfs
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid)) and 
                        col in range(len(grid[0])) 
                        and grid[row][col] == 1 ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1









        
        