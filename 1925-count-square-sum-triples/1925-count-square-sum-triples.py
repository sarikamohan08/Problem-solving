class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            for j in range(1,i):
                k=sqrt(i**2+j**2)
                if int(k)==k and k<=n: ans+=2
        return ans