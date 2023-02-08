class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=cost.copy()
        dp.append(0)
        dp=dp[::-1]
        print(dp)
        for i in range(2,len(dp)):
            print(dp[i]+dp[i-1],dp[i]+dp[i-2])
            dp[i]=min(dp[i]+dp[i-1],dp[i]+dp[i-2])
        print(dp)
        return min(dp[-1],dp[-2])