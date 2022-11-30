from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        # We use a hashmap which maps to lists.
        word_to_count_map = defaultdict(list)
        for s in strs:
            # Instantiate 26 0's in a list.
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            # Lists cannot be keys..            
            word_to_count_map[tuple(count)].append(s)
        
        return word_to_count_map.values()

sol = Solution()

sol.groupAnagrams(["ant", "tan"])
            
