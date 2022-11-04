class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set('aeiouAEIOU')
        i, j = 0, len(s) - 1
        s = list(s)
        while i < j:
            while i < j and s[i] not in v:
                i += 1
            while i < j and s[j] not in v:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)