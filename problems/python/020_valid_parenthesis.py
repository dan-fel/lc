class Solution:
    def isValid(self, s: str) -> bool:
        table = {')' : '(', '}' : '{', ']' : '['}        
        stack = []

        for c in s:
            if c in table:
                if stack and stack[-1] == table[c]:
                    stack.pop()
                else:
                    return False
            else:                
                stack.append(c)

        if len(stack) == 0:
            return True

        return False        

sol = Solution()

print(sol.isValid('({{})'))
print(sol.isValid('((()))'))
print(sol.isValid('((())'))
