class Solution:
    def reverse(self, x: int) -> int:
        rev, isPositive = 0, x > 0  # check if x is positive, make it positive it is not
        if not isPositive: x = -1 * x
        #rev=0
        while(x!=0):
            y=x%10
            rev=rev*10+y
            x=x//10
            
        if rev >= 2**31:    # check condition
            return 0
        
        return rev if isPositive else -1 * rev
            
            