class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alp="abcdefghijklmnopqrstuvwxyz"
        dc={}
        for i in range(26):
            dc[order[i]]=alp[i]
        for i in range(len(words)):
            a=[]
            for x in words[i]:
                a.append(dc[x])
            words[i]="".join(a)
        return words==sorted(words)