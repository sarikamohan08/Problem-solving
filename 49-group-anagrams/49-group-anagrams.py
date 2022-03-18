class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strssorted = [''.join(sorted(x)) for x in strs]
        
        dictionary = {}
        for i,string in enumerate(strssorted):
            if string not in dictionary:
                dictionary[string] = [strs[i]]
            else:
                dictionary[string].append(strs[i])
    
        return list(dictionary.values())