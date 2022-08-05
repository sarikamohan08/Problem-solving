class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1 for _ in range(len(nums))]
        n=len(nums)
        p=1

        for i in range(len(l)):
            l[i]=p
            p=p*nums[i]
        p=1
        for i in reversed(range(len(l))):
            l[i]*=p
            p=p*nums[i]
        return l