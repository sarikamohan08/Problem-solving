class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        start = 0
        end = len(nums) - 1
        
        while start <= end:
            index = (end + start) // 2
                        
            if nums[index] > target:
                end = index - 1
            else:
                start = index + 1
                
        return start