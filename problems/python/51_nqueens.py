from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('.')
            board.append(row)

        def is_intersecting(i, j):
            x, y = i, j
            while x >= 0:                
                if board[x][y] == 'Q':
                    return True
                x -= 1
                
            x = i
            while x < n:
                if board[x][y] == 'Q':
                    return True
                x += 1
            
            x, y = i, j            
            while y < n:                         
                if board[x][y] == 'Q':
                    return True
                y += 1
            
            y = j
            while y >= 0:                
                if board[x][y] == 'Q':
                    return True
                y -= 1
            
            x, y = i, j            
            while x >= 0 and y >= 0:                
                if board[x][y] == 'Q':
                    return True
                x -= 1
                y -= 1
                
            x, y = i, j            
            while x < n and y < n:
                if board[x][y] == 'Q':
                    return True
                x += 1
                y += 1 
            
            return False

        res = []                        
        def backtrack(i, j, qs):
            print(qs)            
            if (i >= n or j >= n) and qs == 0:
                print("bansai")
                return 
            elif i >= n or j >= n and qs != 0:
                return            
            elif qs == 0:
                print("bansai")
                return
            
            board[i][j] = 'Q'
            
            if is_intersecting(i, j):
                board[i][j] = '.'
                backtrack(i + 1, j, qs)    
                backtrack(i, j + 1, qs)
                backtrack(i + 1, j + 1, qs)            
            else:
                board[i][j] = 'Q'
                backtrack(i + 1, j, qs - 1)    
                backtrack(i, j + 1, qs - 1)
                backtrack(i + 1, j + 1, qs - 1)            
                
             # go to next possible piece which does not intersect.
            board[i][j] = '.'
            
        backtrack(0,0, n)
# Q . . .
# . Q . .
# . . Q .
# . . . Q                       

sol = Solution()
sol.solveNQueens(4)