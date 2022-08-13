class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0:
            return 0
        if n == 0 or x == 1:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        if n % 2 == 0:
            return self.myPow(x, n//2) ** 2
        else:
            return self.myPow(x, n//2) * self.myPow(x, (n//2) + 1)