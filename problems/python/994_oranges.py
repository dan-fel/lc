from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: 
            return
        
        queue = deque()
        visited = set()

        rows, cols = len(grid), len(grid[0])

        o_ct = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    o_ct += 1

        while queue:
            p = o_ct
            o_ct = 0
            for i in range(p):
                (r,c) = queue.popleft()
                
                if grid[r][c] == 1:
                    queue.append((r,c))
                    o_ct += 1





        # Find all rotten oranges then do breath first search from all of them.
        # Keep count of how many oranges exist in each step and increase it
        # Add visited rotten oranges and other oranges to visited set
        


#print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
#print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
#print(Solution().orangesRotting([[0, 2]]))
print(Solution().orangesRotting([[0]]))

        