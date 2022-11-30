from typing import List

class Solution:    
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        p = 1
        q = 1
        while q < len(nums):            
            if nums[q] == nums[p] and nums[p] > nums[p - 1]:        
                p += 1; q += 1
            elif nums[p] == nums[p - 1] and nums[q] == nums[p]:
                q += 1
            elif nums[p] <= nums[p - 1] and nums[q] > nums[p - 1]:
                nums[p] = nums[q]        
                p +=1 ; q += 1
            elif nums[p] < nums[p - 1] and nums[q] == nums[p - 1]:                
                q += 1                
            else:
                q += 1; p += 1
        return p

sol= Solution()
print(sol.removeDuplicates([1,2]))
print(sol.removeDuplicates([1,2,3,3,3,4,5,5,5,6,6,6,6,6,6,7,8]))

from typing import List

class SolutionBetter:    
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        p = 1
        q = 1
        while q < len(nums):            
            if nums[q] != nums[q-1]:                
                nums[p] = nums[q]
                p += 1
                q += 1          
            else:
                q += 1
        return p
        

solbetter= SolutionBetter()
print(solbetter.removeDuplicates([1,2]))
print(solbetter.removeDuplicates([1,2,3,3,3,4,5,5,5,6,6,6,6,6,6,7,8]))

                
