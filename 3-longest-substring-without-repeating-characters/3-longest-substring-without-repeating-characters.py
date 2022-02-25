class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:                 #returnng the special case
		
            return 0
        j,list1=0,[]                    #initialisng variables
		
        for i in range(len(s)):         #starts 1st and only loop
		
            if s[i] in s[j:i]:          #checks if this "i"th character is in previous "j"th to < "i"th characters.
			
                ind = s[j:i].index(s[i])#this is the heart, what we are doing is lets say the string is
				                        #"abcabcbb", this line will trigger only when 2nd "a" is found 
				                        #in previous "abc", we take index of first a, and set it to j and
				                        #add 1, so now we will be looking for 2nd "b" in "bca", because we
				                        #cut the window after a, meanwhile we are keeping track of length 
				                        #from our else statement
										
                j = ind + j +1          #keeping "j" updated with itself
				
            else:
                list1.append(i-j+1)     #if none was found we increase length of string and put it in list1.
				
        return max(list1)   