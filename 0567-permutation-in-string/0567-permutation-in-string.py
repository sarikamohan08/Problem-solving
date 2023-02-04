class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d1 = {}
        for i in s1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        win = len(s1)
        for i in range(len(s2)-win+1):
            d2 = {}
            j=i+(win)
            print(j)
            for i in s2[i:j]:
                if i in d2:
                    d2[i] += 1
                else:
                    d2[i] = 1
            if d2 == d1:
                return True
        return False