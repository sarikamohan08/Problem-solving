class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = []
        for i in words[0]:
            if all(i in j for j in words):
                l.append(i)
                words = [k.replace(i,'',1) for k in words]
        return(l)
        
