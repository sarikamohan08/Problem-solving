class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if (len(nums) != k):
            n = len(nums) - k
            if (n < 0):
                n = abs(n)
                n = len(nums) - n
            temp = nums[n:len(nums)]
            nums[n-1:len(nums)] = nums[0:n]
            nums[0:n-1] = temp