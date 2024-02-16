from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            s1 = -heapq.heappop(max_heap)
            s2 = -heapq.heappop(max_heap)

            if s1 < s2:
                heapq.heappush(max_heap, -(s2 - s1))
            elif s1 > s2:
                heapq.heappush(max_heap, -(s1 - s2))            

        if not max_heap:
            return 0
        else:
            return -max_heap[0]
        

sol = Solution()
print(sol.lastStoneWeight([2,7,4,1,8,1]))

