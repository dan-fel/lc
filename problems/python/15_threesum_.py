from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        nums = sorted(nums)        
        res = []        

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while l < r:                
                sum = nums[l] + nums[r]
                if sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum > target:
                    r -= 1
                else:                    
                    l += 1
                    
        return res

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 0, 0]))
print(sol.threeSum([0, 0, 0, 0]))
print(sol.threeSum([-2, 0, 2]))

#print(sol.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
print(sol.threeSum([-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]))
# [ [-2, -1, 3], [-3, 1, 2]]
#[[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]