from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Left pointer finds a zero, append  
        # 2.
        l = 0

        for r in range(len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[l] != 0:
                l += 1
        
             

sol = Solution()
arr = [0, 1, 0, 2, 3, 0, 4]
print(sol.moveZeroes(arr))
print(arr)
