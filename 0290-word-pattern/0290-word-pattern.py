class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=len(pattern)
        t=s.split(" ")
        if l!=len(t):
            return False
        d={}
        for i in range(l):
            if(pattern[i] in d):
                if(d[pattern[i]]!=t[i]):
                    print(d)
                    return False
                else:
                    continue
            elif t[i] in d.values():
                print(d)
                return False
            d[pattern[i]]=t[i]
            print(d)
        return True

            