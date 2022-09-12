class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        print(image[0][::-1])
        img=[]
        n=len(image)
        for i in range(n):
            image[i]=image[i][::-1]
            for j in range(len(image[i])):
                image[i][j]^=1
                print(image)
        return image