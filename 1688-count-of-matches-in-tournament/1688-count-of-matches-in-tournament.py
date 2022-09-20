class Solution:
    def numberOfMatches(self, n: int) -> int:       
        total=[]
        while(n!=1):
            if(n%2==0):
                match=n/2
                total.append(match)
                n=n/2
            else:
                match=int(n/2)
                total.append(match)
                n=int(n/2)+1
        return int(sum(total))