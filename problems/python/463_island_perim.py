from typing import List

# Go through each row in the grid.
# For each row that is part of the island, check in every direction if there is more land there or not and update perimeter accordingly.
# O(n * m) where n is the number of columns in the grid and m is the number of rows.
# Each piece of land only consists of constant work.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:        
        perimeter = 0
        grid_height = len(grid)
        grid_width = len(grid[0])

        for i in range(0, grid_height):
            for j in range(0, grid_width):
                if grid[i][j] == 1:                    
                    if j+1 >= grid_width:
                        perimeter += 1
                    elif grid[i][j+1] == 0:            
                        perimeter += 1
                    if j-1 < 0:
                        perimeter += 1
                    elif grid[i][j-1] == 0:            
                        perimeter += 1
                    if i+1 >= grid_height:
                        perimeter += 1
                    elif grid[i+1][j] == 0:            
                        perimeter += 1
                    if i-1 < 0:
                        perimeter += 1
                    elif grid[i-1][j] == 0:            
                        perimeter += 1                    
        
        return perimeter        

sol = Solution()
sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])