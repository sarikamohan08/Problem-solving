class Solution:
    def arrangeCoins(self, n: int) -> int:
        result = 0
        for i in range(1,n+1):
            n -= i
            if n >= 0:
                result += 1
            else:
                break
        return result