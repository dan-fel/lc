from typing import List
class Solution:
    def swap(self, nums1: List[int], index1, nums2: List[int], index2):
        temp = nums1[index1]
        nums1[index1] = nums2[index2]
        nums2[index2] = temp

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:                
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m - 1
        q = n - 1         
        last = len(nums1) - 1

        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[last] = nums1[p]                
                p -= 1
            else:
                nums1[last] = nums2[q]                
                q -= 1            
            last -= 1

        while q >= 0:
            nums1[last] = nums2[q]                
            q -= 1                        
            last -= 1
        print(nums1)


        

                

sol = Solution()
sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
#sol.merge([1], 1, [], 0)
#sol.merge([0], 0, [1], 1)



        