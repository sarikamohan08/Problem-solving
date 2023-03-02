class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(1, len(nums)+1, 2):
            ans += nums[-i-1]

        return ans