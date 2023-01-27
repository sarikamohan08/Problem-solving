class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Check if current word can be made from smaller words
        def check(word):
            if word in s:
                return True
            # If prefix is seen, recurse on rest of word
            return any(check(word[i:]) for i in range(1, len(word)) if word[:i] in s)
        
        s = set()
        res = []
        for word in sorted(words, key=lambda x:len(x)):
            if check(word):
                res.append(word)
            s.add(word)
        return res