'''
-> use bfs with set and queue to keep visited count and process elements 
-> set rows, cols, set and queue
-> def addCell, use this to eliminate OOB, visited and walls out
-> after edge case elimination, add to set and queue
-> iterate through all elements and add to visited and append
-> do the bfs by popping from the queue, assigning dist and going in 4 directions
'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        # checking OOB conditions
        def addCell(r, c):
            if (min(r, c) < 0 or c == COLS or r == ROWS or grid[r][c] == -1 or (r, c) in visit):
                return 
            visit.add((r, c))
            q.append([r, c])

        
        # iterate and get all gates appended to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append([r, c])
        
        # initialise dist and assign to neighbours
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
