class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
            
        while(columnNumber):
            columnNumber -= 1
            charValue = (columnNumber % 26) 
            columnNumber //= 26
            
            result = chr(charValue + ord('A')) + result
            
        return result