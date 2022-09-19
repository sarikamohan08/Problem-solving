class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        myset = set()
        for word in words:
            s = ""
            for c in word:
                s += morse[ord(c) - 97]
            myset.add(s)
        return len(myset)