from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:            
            if t.isdigit() or '-' in t and len(t) > 1:
                stack.append(t)
            if t == "+":                
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2) + int(v1))
            if t == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2) - int(v1))
            if t == "*":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2) * int(v1))
            if t == "/":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(int(v2) / int(v1)))
        return stack[0]

sol = Solution()

print(sol.evalRPN(["4", "-13", "5", "+", "+"]))
print(sol.evalRPN(["10", "0", "/"]))

            

