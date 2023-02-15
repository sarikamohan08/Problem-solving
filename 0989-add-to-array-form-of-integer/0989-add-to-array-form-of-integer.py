class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=''
        new = []
        for i in num:
            s+=str(i)
        s = int(s) + k
        for i in str(s):
            new.append(int(i))
        return(new)