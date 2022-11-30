from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[0], nums[0]

        fast = nums[nums[fast]]        
        slow = nums[slow]

        while fast != slow:                        
            fast = nums[nums[fast]]            
            slow = nums[slow]
                
        begin, intersect = nums[0], fast        
        
        # Use Floyd's cycle-detection        
        while begin != intersect:
            begin = nums[begin]
            intersect = nums[intersect]

        return intersect
                
sol = Solution()
print(sol.findDuplicate([1,4,4,2,4]))
print(sol.findDuplicate([1,3,4,2,2]))
print(sol.findDuplicate([3,1,3,4,2]))
#print(sol.findDuplicate([1,4,4,2,4]))
#print(sol.findDuplicate([1,4,4,2,4]))

