class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        result = 1
        k = 9
        m = 9  # The number of unique n-digit numbers will be recorded here
        for i in range(n):
            result += m
            m *= (k - i)
        return result