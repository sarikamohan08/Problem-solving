class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g == [] or s == []:
            return 0
        else:
            g.sort()
            s.sort()
            out = 0
            for j in range(len(s)):
                if out < len(g) and s[j] >= g[out]:
                    out += 1
            return out