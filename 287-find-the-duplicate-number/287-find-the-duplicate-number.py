class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #n=len(nums)
        res={}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        for j in res:
            if(res[j]>=2):
                return j
        
            
        