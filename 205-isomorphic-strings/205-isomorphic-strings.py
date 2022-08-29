class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
            #print(map1)
        for idx in t:
            map2.append(t.index(idx))
            #print(map2)
        #print(map1)
        #print(map2)
        if map1 == map2:
            return True
        return False