class Solution:
    def climbStairs(self, n: int) -> int:
        self.M = {}

        return(self.rec(n))
    def rec(self, n: int) -> int:
        # Base cases.
        if n == 0:
            return 1
        elif n < 0:
            return 0
        
        if self.M.get(n):
            print("using memo")
            return self.M.get(n)
        else:            
            result = self.rec(n-1) + self.rec(n-2)
            self.M[n] = result
            return result

sol = Solution()

class SolutionBottomUp:
    def climbStairs(self, n: int) -> int:
        one, two= 1, 1

        for i in range(n-1):
            sum = one + two
            two = one
            one = sum

        return one
        



        
    
    

sol = Solution()

print(sol.climbStairs(20))

sol = SolutionBottomUp()

print(sol.climbStairs(20))


        



            
