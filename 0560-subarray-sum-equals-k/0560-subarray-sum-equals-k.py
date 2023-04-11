class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = dict()
        result = 0
        curr_sum = 0

        for val in nums:
            curr_sum += val

            if curr_sum == k:
                result += 1

            if curr_sum - k in hm:
                result += hm[curr_sum - k]

            hm[curr_sum] = hm.get(curr_sum, 0) + 1

        return result
 