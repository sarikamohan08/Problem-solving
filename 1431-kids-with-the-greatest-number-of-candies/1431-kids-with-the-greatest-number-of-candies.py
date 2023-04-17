class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n=len(candies)
        l=[]
        maxi=max(candies)
        for i in range(n):
            if(candies[i]+extraCandies>=maxi):
                l.append(True)
            else:
                l.append(False)
        return l