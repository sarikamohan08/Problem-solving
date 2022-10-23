class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res={}
        res1=[0,0]
        for i in nums:
            if i in res:
                res[i]+=1
                res1[0]=i
                
            else:
                res[i]=1
        for i in range(len(nums)):
            if i+1 not in res:
                    print(i+1)
                    res1[1] = i+1
                    return res1
        
