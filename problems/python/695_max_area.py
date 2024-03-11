from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area = 0
        queue = deque()
        visited = set()

        dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                area = 0
                if grid[i][j] == 1:                    
                    queue.append((i,j))
                    visited.add((i,j))
                while queue:                    
                    area += 1
                    max_area = max(max_area, area)                
                    t = queue.popleft()
                    for d in dirs:
                        if t[0] + d[0] >= 0 and t[0] + d[0] < len(grid) and t[1] + d[1] >= 0 and t[1] + d[1] < len(grid[0]):
                            if grid[t[0] + d[0]][t[1] + d[1]] == 1 and (t[0] + d[0], t[1] + d[1]) not in visited:                                                                
                                queue.append((t[0] + d[0], t[1] + d[1]))
                                visited.add((t[0] + d[0], t[1] + d[1]))
        
        return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
g2 = [[1]]
print(Solution().maxAreaOfIsland(grid))
print(Solution().maxAreaOfIsland(g2))
