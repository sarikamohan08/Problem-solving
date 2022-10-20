class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxi=-inf
        res=-inf
        set1=set(nums)
        for n in nums:
            if n>0 and -n in set1 and n>maxi:
                    maxi = n
                    res = n
        return res if res!=-inf else -1
            