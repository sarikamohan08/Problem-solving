class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l=[] 
        for i in range(len(s)): #store the c's index found in s
            if s[i]==c:
                l.append(i) 
        ans=[] #store distance from index i to the closest occurrence of character c in s
        
        #finding distance of i from every c present in s (creating 2 loops)
        
        for i in range(len(s)):
            r=sys.maxsize #firstly declare max_int for every element to be compared from
            for j in l: # c's index
                r=min(r,abs(i-j)) #need to take shortest distance
            ans.append(r) #store final shortest distance
        return ans