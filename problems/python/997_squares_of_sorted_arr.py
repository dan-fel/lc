from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:                
        l, r = 0, len(nums) - 1                
        merged = []
        while l <= r:
            r_sq, l_sq = nums[r]*nums[r], nums[l]*nums[l]                    
            if r_sq < l_sq:            
                merged.append(l_sq)
                l += 1
            else:            
                merged.append(r_sq)
                r -= 1                                    
        return reversed(merged)
                        
sol = Solution()

sol.sortedSquares([-4, -1, 0, 3, 10])


