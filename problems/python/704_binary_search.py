from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:                
        left, right = 0, len(nums) - 1
        
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            
            
            # print("right", right)
            # print("left", left)
            # print("mid", mid)
            # print("nums mid", nums[mid])
            # print("----")
            if target > nums[mid]:                        
                left = mid +1
            elif target < nums[mid]:                
                right = mid -1
            else:
                return mid

        return mid if target == nums[mid] else -1
            


               
            
sol = Solution()
print(sol.search([ 5], 5))
print(sol.search([-1,0,3,5,9,12], 0))
print(sol.search([1,2,3,4,5,6,7], 7))
print(sol.search([-1,0,3,5,9,12], 2))
print(sol.search([1,3,4,5,6,8,12], 15))