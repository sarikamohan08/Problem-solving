class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows,cols=len(mat),len(mat[0])
        
        if rows*cols!= r*c or (rows==r and cols==c):
            return mat
        
        m=[]
        for i in range(rows):
            m+=mat[i]
        
        res=[]
        for i in range(r):
            res.append([m.pop(0) for i in range(c)])
            print(res)
        return res
    
