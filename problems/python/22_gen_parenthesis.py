from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def backtrack(open, closed):
            if open == closed == n:
                print(stack)
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            if closed < n and closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)

        return res

sol = Solution()
print(sol.generateParenthesis(2))
