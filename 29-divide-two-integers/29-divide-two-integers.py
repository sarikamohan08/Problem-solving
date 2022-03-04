class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) ^ (divisor < 0)        

        a, b = abs(dividend), abs(divisor)

        res, aux = 0 , 1        

        

        while a >= b:

            b <<= 1

            aux <<= 1                        

        

        while aux:

            b >>= 1

            aux >>= 1

            if a >= b:

                a -= b

                res += aux

                

        res = -res if neg else res

        

        return min(max(-2**31, res), 2**31 - 1)