class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]
        
        previousRow = self.getRow(rowIndex -1)
        newRow = [None]*(rowIndex +1)
        
        newRow[0] = newRow[-1] = 1
        
        for i in range(1,rowIndex):
            newRow[i] = previousRow[i-1] + previousRow[i]
        
        return newRow