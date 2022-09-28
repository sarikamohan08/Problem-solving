class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ans=""
        vowel = ["a","e","i","o","u","A","E","I","O","U"]
        sentence=sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0] in vowel:
                ans = ans + sentence[i]
            else:
                ans = ans + sentence[i][1:] + sentence[i][0]
            ans = ans + "ma" + "a"*(i+1) + " "

        return ans[:-1]