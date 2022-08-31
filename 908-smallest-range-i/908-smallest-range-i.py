class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        n=len(nums)
        min_ele=min(nums)
        max_ele=max(nums)
        for i in range(n):
            if(min_ele+k>max_ele-k):
                return 0
            else:
                return (max_ele-k)-(min_ele+k)
    