class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        for i in range(len(nums)-2):# loop will check ith,(i+1)th,(i+2)th term
            if nums[i]<nums[i+1]+nums[i+2]:#check for triangle condition (a+b>c)
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
    