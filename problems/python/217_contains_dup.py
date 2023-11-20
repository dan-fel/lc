from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        currentNums = {}
        for num in nums:
            if num not in currentNums:
                currentNums[num] = 1
            else:
                return True            
        return False
    
sol = Solution()

print(sol.containsDuplicate([1,2,3,4]))


        