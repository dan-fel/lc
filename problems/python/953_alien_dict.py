from typing import List
# Use a hashmap for lookups in ordering.
# Use a sliding window of 2 along the list of words.
# If two characters are not equal then check their order.
# O(N)

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}

        index = 0
        for c in order:
            order_dict[c] = index
            index += 1                
        for i in range(0, len(words)-1):                        
            for j in range(0, len(words[i])):                
                if j == len(words[i+1]):
                    return False
                c1 = words[i][j]
                c2 = words[i+1][j]
                if c1 != c2:                                       
                    if order_dict[c1] > order_dict[c2]:                    
                        return False
                    break         
        return True        

sol = Solution()
print(sol.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))