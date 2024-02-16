from typing import List
from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point):
            return sqrt(point[0] * point[0] + point[1] * point[1])

        distance_and_points = [(-distance(p), p) for p in points]        
        res = []
        for p in distance_and_points:
            if len(res) < k:
                heapq.heappush(res, p)
            elif -p[0] < -res[0][0]:                
                heapq.heappop(res)
                heapq.heappush(res, p)

        return [p[1] for p in res]        

        


sol = Solution()

print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))



        