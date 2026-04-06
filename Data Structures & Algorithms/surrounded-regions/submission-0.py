'''
-> Reverse thinking the whole thing
-> marking the regions that are not surrounded
-> create dfs helper function to mark O -> T and iterate through outer only to mark them
-> then iterate through everything and mark those without O -> X
-> then finally revert from T -> O
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        # marking the regions that are not surrounded (O -> T)
        def capture(r, c):
            if (r<0 or r == ROWS or c<0 or c == COLS or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)


        # iterate through everything and mark those without O -> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # finally revert from T -> O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

'''
Time Complexity : O(ROWS * COLS)
Space Complexity : O(ROWS * COLS)
'''

