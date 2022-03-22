from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, len(nums)+1):
            temp = list(combinations(nums, i))
            res.extend(list(x) for x in temp)
        res.append([])
        return res