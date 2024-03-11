
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 0, k

        while l <= r:
            mid = l + (r - l) // 2
            h_c, i = 0, 0
            while h_c < h and i < len(piles):
                h_c += math.ceil(piles[i] / mid)
                i += 1
            
            if h_c <= h and i == len(piles):
                print("found new min:", mid)
                k = min(k, mid)
                r = mid - 1
            else:
                print("doing", mid)
                l = mid + 1

            print(l, r)
        return k


sol = Solution()
print(sol.minEatingSpeed([332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184], 823855818))
#print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6))
#print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))
#print(sol.minEatingSpeed([3,6,7,11], 8))