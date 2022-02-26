class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        i, j = sr, sc
        
        # store the value to compare later whether or not the current index needs updating
        originalColor = image[i][j]
        self.recFill(image, i, j, newColor, originalColor)
        return image

    def recFill(self, image, i, j, newColor, originalColor):
        """
        - The Following conditions should be checked
        1. is the current i value less than 0
        2. is the current j value less than 0
        3. is the current i value greater than the total rows
        4. is the current j value greater than the cols
        5. is the current indexes i and j both updated with the newColor
        6. the current i and j index dont need to be updated, since they are not the same color as that of image[sr][sc]
        """
        if i < 0 or j < 0 or i > len(image) - 1 or j > len(image[0])-1 or image[i][j] == newColor or image[i][j] != originalColor:
            return
        
        image[i][j] = newColor
        self.recFill(image, i-1, j, newColor, originalColor)
        self.recFill(image, i+1, j, newColor, originalColor)
        self.recFill(image, i, j+1, newColor, originalColor)
        self.recFill(image, i, j-1, newColor, originalColor)
        