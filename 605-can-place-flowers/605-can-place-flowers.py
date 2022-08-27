class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        flowerbed = [0] + flowerbed + [0]
        print(flowerbed)
        for i in range(1,len(flowerbed)-1):
            #print(i)
            if(flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0):
                flowerbed[i]=1
                c+=1
        
        if(c>=n):
            return True
        
        