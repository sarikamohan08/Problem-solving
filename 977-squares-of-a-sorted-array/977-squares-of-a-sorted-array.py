class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        a=[]
        for i in range(n):
            a.append(nums[i]*nums[i])
        
        sorted_array=sorted(a)
        return sorted_array
            