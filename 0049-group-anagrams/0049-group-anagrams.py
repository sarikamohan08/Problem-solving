class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strssorted = [''.join(sorted(x)) for x in strs]
        
        dictionary = {}
        for i,string in enumerate(strssorted):
            if string not in dictionary:
                dictionary[string] = [strs[i]]
            else:
                dictionary[string].append(strs[i])
    
        return list(dictionary.values())