class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #time complexity o(n^2)
        
        #for i in range(len(matrix)):
         #   for j in range(len(matrix[0])):
          #      if (matrix[i][j]==target) :
           #         return True
        #return False
        
        
        #time complexity o(n)
        
        i=0
        j=len(matrix[0])-1
        n=len(matrix)
        while(i<n and j>=0):
            if (target==matrix[i][j]):
                return True
            elif(target<matrix[i][j]):
                j=j-1
            else:
                i+=1
        return False

