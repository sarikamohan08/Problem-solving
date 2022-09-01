class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left,right+1):
            flag=True
            for j in str(i):
                if int(j)==0:
                    flag=False
                    break
                if i%int(j)!=0:
                    flag=False
            if flag==True:
                l.append(i)
        return l