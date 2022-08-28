class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)): 
            if i>0 and nums[i-1]==nums[i]:
                continue

            l=i+1
            r=len(nums)-1
            ans = []
            while l<r:                
                if nums[l]+nums[r]+nums[i]==0:
                    ans=[nums[i],nums[l],nums[r]]
                    out.append(ans)
                    l+=1
                    while nums[l-1]==nums[l] and l<r:
                        l+=1
                elif nums[l]+nums[r]+nums[i]<0:
                    l+=1
                else:
                    r-=1
        return out
                        