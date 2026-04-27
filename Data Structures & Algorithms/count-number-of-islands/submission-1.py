class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # init number of islands, rows, cols
        rows = len(grid)
        cols = len(grid[0])
        num_island = 0

        # dfs function
        def dfs(r, c):
            # base case
            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                grid[r][c] == "0"
            ):
                return 
            
            grid[r][c] = "0"
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(r+dr, c+dc)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_island += 1

        return num_island