class Solution:
    # O(n) solution
    def arrangeCoins(self, n: int) -> int:
        i = 0
        rows = 0
        
        while True:
            i += 1
            n = n - i
            if n < 0:
                return rows
            if n == 0:
                rows += 1
                return rows
            rows += 1

        return rows
    def arrangeCoinsFast(self, n: int) -> int:
        coins = n
        l, r =0, n

        while l <= r:
            m = (l + r) // 2
            print("mid:", m)
            required_coins = (m * (m + 1)) / 2

            if required_coins > coins:
                print("kok")
                r = m - 1
            elif required_coins < coins:             
                return r   
                print("Moving left", m +1)
                l = m + 1
            else:                
                return m

        return r
        


sol = Solution()
print(sol.arrangeCoins(9))
print(sol.arrangeCoins(5))
# print(sol.arrangeCoins(35))
# print(sol.arrangeCoins(41))

print(sol.arrangeCoinsFast(9))
print(sol.arrangeCoinsFast(5))
# print(sol.arrangeCoinsFast(35))
# print(sol.arrangeCoinsFast(41))

