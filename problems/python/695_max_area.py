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
                while queue:
                    print(area)
                    area += 1
                    max_area = max(max_area, area)
                    t = queue.popleft()
                    for d in dirs:
                        if grid[t[0] + d[0]][t[1] + d[1]] == 1:
                            queue.append((t[0] + d[0], t[1] + d[1]))
                            visited.add((t[0] + d[0], t[1] + d[1]))
        
        return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
