from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = 1
        
        left_mulsum_list = []
        for n in nums:
            s *= n
            left_mulsum_list.append(s)

        right_mulsum = 1        
        i = len(nums) - 1

        while i >= 0:          
            if i - 1 < 0:   
                pes = right_mulsum
            else:
                pes = left_mulsum_list[i-1] * right_mulsum            
            right_mulsum *= nums[i]            
            nums[i] = pes            
            i -= 1        

        return nums


sol = Solution()

print(sol.productExceptSelf([1,2]))

print(sol.productExceptSelf([1,2,3]))
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([1,2,3,4,5,6]))
print(sol.productExceptSelf([1]))

