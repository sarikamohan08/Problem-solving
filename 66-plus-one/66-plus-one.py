class Solution(object):
    """"
    def stich(self, arr):
        res = ""
        for num in arr:
            res += str(num)
        return int(res) + 1
        
    def split(self, nums):
        return [num for num in str(nums)]
        
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.split(self.stich(digits))
    """
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