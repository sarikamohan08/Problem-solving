class Solution:
    def sortSentence(self, s: str) -> str:
        splited_string = s[::-1].split() 
        splited_string.sort() 
        res = [] 
        for word in splited_string:
            res.append(word[1:][::-1])
        return " ".join(res)