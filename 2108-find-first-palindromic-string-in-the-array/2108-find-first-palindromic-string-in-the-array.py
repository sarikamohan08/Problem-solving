class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        n=len(words)
        l=[]
        for i in range(n):
            check=words[i][::-1]
            if(words[i]==check):
                return words[i]
                
            
        
        return ""