class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num: return str(num)
        if num >= 0:
            sign = ""
        else:
            sign = "-"
            num = -num 
        res = []
        while num > 0:
            res.append(str(num % 7))
            num //= 7
        res.append(sign)
        return ''.join(reversed(res))