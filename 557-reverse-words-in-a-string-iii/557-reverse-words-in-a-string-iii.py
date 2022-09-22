class Solution:
    def reverseWords(self, s: str) -> str:
        lis=[]
        #for i in s:
        #return s.split()  
        s=s.split()
        n=len(s)
        print(n)
        for i in range(n):
            s[i]=s[i][::-1]
            lis.append(s[i])
        sen=" ".join(lis)
        return(sen)