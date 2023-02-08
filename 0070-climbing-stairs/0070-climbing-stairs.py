class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n+1)
        print(dp)
        for i in range(2, n+1):
            print(dp[i-1])
            print(dp[i-2])
            dp[i] = dp[i-1] + dp[i-2]
            print(dp[i])
        return dp[-1]