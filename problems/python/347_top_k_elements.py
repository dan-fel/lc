from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary
        H = {}
        for n in nums: # O(n)
            # Ensures no exception are thrown.
            H[n] = H.get(n, 0) + 1

        print(H)
        
        # Apply bucket sorting.
        # The input can max be len(nums) which means that we
        # have a upper bound on the frequency of any element, (i.e., len(nums))

        # Use a new hashmap which maps occurences x -> list of integers which occur x times.
        # When returning k top frequent integers, start from the right.

        B = defaultdict(list)
        R = []
        K = k

        # Initialize buckets
        for i in range(0, len(nums)):
            B[i] = []

        # Append to buckets
        for h in H:
            B[H.get(h)].append(h)
    
        # Start from right and pop until K is 0.
        for i in range(len(nums), 0, -1):            
            while B[i] and K != 0:
                R.append(B[i].pop())
                K -= 1
        
        return R
            
sol = Solution()

print(sol.topKFrequent([4,4,4,4,1,1,1,2,2,3,3, 100], 5))


