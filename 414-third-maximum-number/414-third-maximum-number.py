class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums = sorted(list(set(nums)))
        n=len(nums)
        if(n>2):
            return nums[-3]
        else:
            return nums[-1]