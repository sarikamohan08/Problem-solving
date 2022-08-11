class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def getSubset(i):
            return [[], [i]]
        res = getSubset(nums[0])
        for n in nums[1:]:
            res = [i + j for i in res for j in getSubset(n)]
        return res