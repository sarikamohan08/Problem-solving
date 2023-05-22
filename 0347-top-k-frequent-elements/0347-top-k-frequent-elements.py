class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num=Counter(nums)
        return sorted(num, key = num.get, reverse=True)[:k]
            