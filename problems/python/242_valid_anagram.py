from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_a = {}    
        table_b = {}
        # O(n) solution.

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            table_a[s[i]] = 1 + table_a.get(s[i], 0)            
            table_b[s[i]] = 1 + table_b.get(s[i], 0)            

        for e in table_a:
            if table_a.get(e) != table_b.get(e):
                return False
            
        return True
        



sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("nagaram", "ada"))

class SolutionTwo:
    def isAnagram(self, s: str, t: str) -> bool:
        # This solution assumes that sorted uses a O(n log n) sorting implementation and is relatively memory efficient.
        return sorted(s) == sorted(t)
        


        