from typing import List
from typing import Dict

class Solution:
    def fasterTwoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in enumerate(nums):
            val = target - i[1]
            
            value_from_map = hash_map.get(val)
            if value_from_map is None:
                hash_map[i[1]] = i[0]
            else:
                return [hash_map.get(val), i[0]]
            
    def createHashTable(self, nums: List[int]) -> Dict[int, int]:
        hash_table = {}
        for idx in range(0, len(nums)):
            hash_table[nums[idx]] = idx

        return hash_table


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = self.createHashTable(nums)

        for idx in range(0, len(nums)):
            val_needed = target - nums[idx]

            hash_idx = hash_table.get(val_needed)
            if hash_idx != idx and hash_idx is not None:
                return [idx, hash_idx] 


sol = Solution()
print(sol.twoSum([2,1,5,3], 4))
print(sol.fasterTwoSum([2,1,5,3], 4))

        