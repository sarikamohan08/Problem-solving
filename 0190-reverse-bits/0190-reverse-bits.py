class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_int=0

        for i in range(32):
            if(n%2==1):
                reversed_int+=1
            reversed_int*=2
            n=n//2
        
        return reversed_int//2