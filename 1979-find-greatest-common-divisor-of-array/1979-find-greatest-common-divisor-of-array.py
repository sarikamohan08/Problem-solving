class Solution:
    def findGCD(self, nums: List[int]) -> int:
        res=0
        def gcd(a,b):
            if(b==0):
                return abs(a)
            else:
                return gcd(b,a%b)
                
        mi=min(nums)
        ma=max(nums)
        res=gcd(mi,ma)
        return res