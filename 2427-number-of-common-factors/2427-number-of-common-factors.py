class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n=max(a,b)
        l=0
        for i in range(1,n+1):
            if(a%i==0 and b%i==0):
                l+=1
        return l
        
        
            