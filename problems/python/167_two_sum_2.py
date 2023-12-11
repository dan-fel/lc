from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum > target: 
                r -= 1
            else:
                l += 1
            
        return []

sol = Solution()
print(sol.twoSum([5,25,75], 100))
print(sol.twoSum([2,3,4], 6))
print(sol.twoSum([-1,0], -1))
print(sol.twoSum([2,7,11,15], 9))