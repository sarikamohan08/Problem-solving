class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for i in costs: 
            if coins<i or coins==0: 
                return c 
            else: 
                c+=1 
                coins-=i 
        return c