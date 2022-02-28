class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = len(nums)//2
        return sorted(nums)[mid]        

            