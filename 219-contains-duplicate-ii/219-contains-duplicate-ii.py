class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicset = {}
        for i in range(len(nums)):
            if nums[i] in dicset: return True
            dicset[nums[i]]= i
            if len(dicset) > k:
                del dicset[nums[i-k]] 
        return False