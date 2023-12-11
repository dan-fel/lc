from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set (nums)
        longest = 0
        
        for n in num_set:
            if n - 1 not in num_set:
                length = 0

                while n + length in num_set:
                    length += 1
                    
                longest = max(length, longest)
        return longest

                                
sol = Solution()
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(sol.longestConsecutive([100,4,200,1,3,2]))