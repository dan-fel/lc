from typing import List

# Merge sort:

# 1. Recursive solution.
# 2. Split the array in the middle // 2 and split form 0:pivot and pivot:
# 3. Recurse down until we reach a single element
# 4. As we bubble up create and return a new list with sorted elements.

class Solution:
    def merger(self, nums1: List[int], nums2: List[int]):

        l, r = 0, 0

        res = []

        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        
        if r < len(nums2):
            res += nums2[r:]
        elif l < len(nums1):
            res += nums1[l:]
        
        return res
            
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        pivot = len(nums) // 2

        l = self.sortArray(nums[0:pivot])
        r = self.sortArray(nums[pivot:])

        return self.merger(l, r)

sol = Solution()
#print(sol.sorter([1,3,5], [2,4,6]))
print(sol.sortArray([1,3,5,2,4,6,22,33,44,55,66,77]))
    
            
