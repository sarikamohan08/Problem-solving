class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 1
        if x < 0:
            a = -1
            x = abs(x)
        s = 0
        while x:
            s *= 10
            s += x%10
            x //= 10
        s = a*s
        if s < -2**31 or s>2**31-1:
            return 0
        return s