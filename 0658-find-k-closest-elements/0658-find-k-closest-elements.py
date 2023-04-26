class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=[]
        n=len(arr)
        i,j=0,0
        
        if(x<arr[0]):
            i,j=0,k-1
        elif(x>arr[-1]):
            i,j=n-k,n-1
            # print("i",i)
            # print("j: ",j)
        else:
            i,j=0,n-1
            while((j-i+1 )>k):
                a=abs(arr[i]-x)
                b=abs(arr[j]-x)
                if(a<=b):
                    j=j-1
                else:
                    i=i+1
        return arr[i:j+1]