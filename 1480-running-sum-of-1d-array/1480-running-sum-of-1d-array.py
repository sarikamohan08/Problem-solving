class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[]
        sum1=0
        for i in range(0,n):
            l.append(sum1+nums[i])
            sum1=l[i]
        return l