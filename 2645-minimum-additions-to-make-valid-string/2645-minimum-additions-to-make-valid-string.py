class Solution:
    def addMinimum(self, word: str) -> int:
                   
        s = "abc"
        i,j,count = 0, 0, 0
        while j < len(word) :
            if i == 3 :
                i = 0
            if word[j] != s[i] :
                count += 1
            else :
                j += 1
            i += 1
        return count + (3-i)