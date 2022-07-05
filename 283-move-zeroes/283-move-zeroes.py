class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_place = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_place] = nums[zero_place], nums[i]
                zero_place += 1
