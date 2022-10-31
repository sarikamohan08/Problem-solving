class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows=len(matrix)
        col=len(matrix[0])
        print(rows,col)
        l=[]
        for i in range(1,rows):
            for j in range(1,col):
                if (matrix[i][j]!=matrix[i-1][j-1]):
                    return 0
        return 1
        
                