class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()[::-1]
        l = []
        for i in st:
            # apending reversed words to l
            l.append(i)
        # printing reverse words
        return(" ".join(l))

