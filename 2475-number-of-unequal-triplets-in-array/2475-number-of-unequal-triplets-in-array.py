class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
            result = 0
            for i in range(len(nums)-2):
                for j in range(i+1,len(nums)-1):
                    for k in range(j+1,len(nums)):
                        if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                            result = result + 1

            return result