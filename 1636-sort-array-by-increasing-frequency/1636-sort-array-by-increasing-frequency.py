class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        return sorted(sorted(nums, reverse=True), key=lambda x: d[x])