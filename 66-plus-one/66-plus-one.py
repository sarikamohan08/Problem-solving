class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arr=digits
        res = ""
        for num in arr:
            res += str(num)
        s=int(res) + 1
        return[num for num in str(s)]