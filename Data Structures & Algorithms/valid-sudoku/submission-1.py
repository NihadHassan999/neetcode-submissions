class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # init rows, cols, boxes
       rows = [set() for _ in range(9)]
       cols = [set() for _ in range(9)]
       boxes = [set() for _ in range(9)]
       # start loop
       for r in range(9):
        for c in range(9):
            val = board[r][c]
            # early none check
            if val == ".":
                continue
            box = (r // 3) * 3 + (c // 3)
            # return false if duplicate
            if val in rows[r] or val in cols[c] or val in boxes[box]:
                return False
            # add value
            rows[r].add(val)
            cols[c].add(val)
            boxes[box].add(val)
       # return true 
       return True