class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d=[]
        l=[]
        for i in range(len(mat)):
            a=[sum(mat[i]),i]
            d.append(a)
            d.sort()
        for i in range(k):
            s=d[i][1]
            l.append(s)
        return l