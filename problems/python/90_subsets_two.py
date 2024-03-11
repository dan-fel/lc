
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:        
        res = []
        cand = []
        nums = sorted(nums)

        def dfs(i): 
            print(cand)
            if i >= len(nums):
                res.append(cand.copy())
                return            
            cand.append(nums[i])
            dfs(i+1)

            cand.pop()
            while i < (len(nums) - 1) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)                        
        dfs(0)

        return res

sol = Solution()
print(sol.subsetsWithDup([1,2,2]))


