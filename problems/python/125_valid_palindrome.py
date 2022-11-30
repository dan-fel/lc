class Solution:
    def isPalindrome(self, s: str) -> bool:        
        left, right = 0, len(s) - 1

        while left < right: 
            if not s[right].isalnum() or s[right].isspace():
                right -= 1
                continue

            if not s[left].isalnum() or s[left].isspace():
                left += 1
                continue

            if s[left].lower() != s[right].lower():                
                return False

            left += 1
            right -= 1

        
        return True


            
            

            



        
        
        

sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("aa"))
print(sol.isPalindrome("ab@a"))
print(sol.isPalindrome("raceacar"))
print(sol.isPalindrome(""))