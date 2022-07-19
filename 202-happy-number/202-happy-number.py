class Solution:
    def isHappy(self, n: int) -> bool:
        seen=[n]
        while (n!=1):
            sum=0
            n=str(n)
            for i in n:
                sum+=int(i)*int(i)
            n=sum
            if(n not in seen):
                seen.append(n)
            else:
                return False
        return True