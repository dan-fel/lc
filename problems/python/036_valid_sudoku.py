# Idea:
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = 9
        rows = 9        

        squares = {(i, j) : set() for i in range(1,4) for j in range(1, 4)}

        row_set = set()
        col_set = set()
        for i in range(0, rows):
            row_set.clear()
            col_set.clear()                
            for j in range(0, cols):
                col_val = board[i][j]
                row_val = board[j][i]


                if row_val in row_set and row_val != '.':
                    return False
                if col_val in col_set and col_val != '.':
                    return False
                
                row_set.add(row_val)
                col_set.add(col_val)

                row_sq_idx = (i + 3) // 3
                col_sq_idx = (j + 3) // 3
                sq_set = squares[(row_sq_idx, col_sq_idx)]
                val = board[i][j]
                if val in sq_set and val != '.':                    
                    return False
                else:
                    sq_set.add(val)             
        return True       

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
sol = Solution()
print(sol.isValidSudoku(board))