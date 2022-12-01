class Solution:
    def halvesAreAlike(self, s: str) -> bool:
            c_1=0
            c_2=0
            v={'a','e','i','o','u','A','E','I','O','U'}
            for x in range(len(s)):
                if x>=(len(s)//2) and s[x] in v:
                    c_2+=1
                elif s[x] in v:
                    c_1+=1
            if c_1==c_2:
                return True
            return False