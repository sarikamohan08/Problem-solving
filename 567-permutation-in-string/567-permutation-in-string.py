class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        k = len(s1)   # length of s1 string
        sorted_s1 = ''.join(sorted(s1))

        n = len(s2)   # length of s2 string

        # we will use the sorting logic to check for permutations.
        # Take s1 = 'acb' and s2 = 'cba'. Now if we sort s1 and s2, 
        # we will get s1 == s2 for every permutation of s2 in s1.

        for i in range(n-k+1):
            # iterating to n-k index for sub strings of length k

            # fetching the possible sub string of length k from index i onwards
            possible_match = ''.join(sorted(s2[i:i+k]))  

            if sorted_s1 == possible_match:
                return True

        return False 