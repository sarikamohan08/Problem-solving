class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        data = []

        while n > 0:
            data.append(n % 2)
            n //= 2

            if len(data) > 1:
                if data[-1] == data[-2]:
                    return False

        return True