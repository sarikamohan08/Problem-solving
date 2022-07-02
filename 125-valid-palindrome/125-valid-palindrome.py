class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        #s1=re.sub(r'[^\w\s]', '', s)
        s1 = s.replace(' ', '')
        s1 = s1.lower()
        s1 = [x for x in s1 if x.isalnum()]
        
        return list(s1)==list(s1)[::-1]
           