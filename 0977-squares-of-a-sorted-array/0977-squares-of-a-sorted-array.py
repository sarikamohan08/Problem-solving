class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range (len(nums)):
            s=nums[i]**2
            l.append(s)
        l.sort()
        return l