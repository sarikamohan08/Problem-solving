class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        s.append("")
        for i in range(len(t)):
            if s[i]!=t[i]:
                return t[i]