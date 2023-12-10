import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_set = set([chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)])
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] not in char_set:
                l += 1
            elif s[r] not in char_set:
                r -= 1            
            elif s[l].lower() == s[r].lower():                
                l, r = l + 1, r - 1
            else:
                return False
        return True
            



sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))