class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        l=[]
        for i in range(1,100001):
            if(i%n==0 and i%2==0):
                l.append(i)
        return min(l)
                