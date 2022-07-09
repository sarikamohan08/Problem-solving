class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l < r:
            m = (l + r)//2
            if m*m == num:
                return True
            elif m*m > num:
                r = m
            else:
                l = m + 1
        return l**1 == num
                
        
       