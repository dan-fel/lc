from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()        
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)

        return False

sol = Solution()

print(sol.containsDuplicate([1,2,3,4,4,5,6,7]))
        