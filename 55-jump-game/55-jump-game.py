class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        flag=1
        if(n==0):
            return False
        if(n==1):
            return True
        reach=nums[0]
        for i in range(n):
            if(i>reach):
                return False
            reach=max(reach,i+nums[i])
        return True
        
