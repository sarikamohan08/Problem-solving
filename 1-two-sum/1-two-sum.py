class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            for j in range(i):
                if(nums[i]+nums[j]==target):
                    l.append(j)
                    l.append(i)
                else:
                    continue
        return l