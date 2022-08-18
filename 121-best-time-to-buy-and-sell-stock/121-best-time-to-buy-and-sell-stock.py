class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        if len(prices)==0:
            return 0
        else:
            profit=0
            minbuy=prices[0]
            for i in range(len(prices)):
                profit=max(prices[i]-minbuy,profit)
                minbuy=min(minbuy,prices[i])
            return profit