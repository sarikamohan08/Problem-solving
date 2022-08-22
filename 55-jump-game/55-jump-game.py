class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        flag=1
        if(n==0):
            return False
        if(n==1):
            return True
        reach=nums[0]
        for i in range(1,n):
            if(i>reach):
                print(i)
                return False
            
            print(i)
            reach=max(reach,i+nums[i])
        return True
        
