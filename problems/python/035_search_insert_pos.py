from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1        
        while left <= right:
            mid = (left + right) // 2  

            if target == nums[mid]:
                return mid
            if target > nums[mid]:                
                left = mid + 1
            else:
                right = mid - 1
        
        return left
            
sol = Solution()
print(sol.searchInsert([1,3,5,6], 0))
print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 7))
