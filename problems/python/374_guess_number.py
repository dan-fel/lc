# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def __init__(self, pick: int):
        self.pick = pick

    def guess(self, num: int) -> int:
        # Our guess is larger than the pick, thus guess must be in lower half.
        if num > self.pick:
            return -1
        # Our guess is less than the pick, thus guess must be in upper half.
        elif num < self.pick:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        left, right = 1, n        
        while True:
            mid = (left + right) // 2

            res = self.guess(mid)
            if res == 0:
                return mid
            if res == -1:
                right = mid - 1
            elif res == 1:
                left = mid + 1

sol = Solution(4)
print(sol.guessNumber(20))
print(sol.guessNumber(15))
print(sol.guessNumber(7))
