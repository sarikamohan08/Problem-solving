class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}  # Dictionary to store characters and their indices
        left = 0  # Left pointer to track the start of the current substring
        max_len = 0  # Maximum length of the substring without repeating characters

        for right in range(len(s)):
            if s[right] not in dic:  # If the current character is not in the dictionary
                max_len = max(max_len, right-left+1)  
            else:
                if dic[s[right]] < left:  # If the character is in the dictionary but its index is before the current substring
                    max_len = max(max_len, right-left+1)  
                else:
                    left = dic[s[right]] + 1  # Update the left pointer to skip the repeated character
            dic[s[right]] = right  # Update the index of the current character in the dictionary

        return max_len