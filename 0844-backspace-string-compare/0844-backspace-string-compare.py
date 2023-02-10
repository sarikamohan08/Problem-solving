class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """"
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=[]    #use this to add only alphabets
        t1=[]    #same as above
        for i in s:
            if i.isalpha():
                s1.append(i)
            elif len(s1)==0:   #if list is empty then don't add anything and continue
                continue
            else:
                s1.pop(-1)    # if you come across the '#' in the list, pop the last element in the new lists created only 
        for i in t:                # for alphabets; i.e s1 and t1 in this case
            if i.isalpha():
                t1.append(i)
            elif len(t1)==0:
                continue
            else:
                t1.pop(-1)
        
        while len(s1)==len(t1):
            return t1==s1    
			