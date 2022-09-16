class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        res=[]
        for i in range(col):
            newmatrix=[]
            for j in range(row):
                newmatrix.append(matrix[j][i])
            res.append(newmatrix)
        return res