class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            x = list(str(i))
            if sum(int(y) for y  in x) %2==0:
                c+=1
        return c
                