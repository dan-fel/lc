from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        
        max_area = 0
        while l < r:
            distance = r - l
            area = min(height[l], height[r]) * distance

            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

