from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(i):                        
            if i >= len(candidates) or sum(comb) >= target:
                return                        
            comb.append(candidates[i])
            s = sum(comb)            
            if s == target:
                res.append(comb.copy())                                                        
            dfs(i)
            comb.pop()            
            dfs(i + 1)
        dfs(0)
        return res
    
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))

        