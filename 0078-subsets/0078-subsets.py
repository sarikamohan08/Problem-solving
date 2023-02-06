class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recSub(nums,res,start,end,lis):
            print(nums,res,start,end,lis)
            res.append(lis)
            if start == end:
                return
            for i in range(start,end):
                recSub(nums,res,i+1,end,lis+[nums[i]])
        recSub(nums,res,0,len(nums),[])      
        return res