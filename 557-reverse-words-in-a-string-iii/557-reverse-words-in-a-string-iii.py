class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        convert_to_list = s.split()
        newlist = []
        for i in convert_to_list:
            newlist.append(i[::-1])
        return ' '.join(newlist)