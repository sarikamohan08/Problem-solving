class Solution:
    def calPoints(self, ops: List[str]) -> int:
        n=len(ops)
        l=[]
        for i in range(n):
            if(ops[i]=="C"):
                l.pop()
               
            elif(ops[i]=="D"):
                l.append(int(l[len(l)-1])*2)
                
            elif(ops[i]=="+"):
                l.append((int(l[len(l)-1]) + int(l[len(l)-2])))
            else:
                l.append(int(ops[i]))
        return sum(l)