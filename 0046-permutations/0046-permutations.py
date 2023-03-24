class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
		
		# Base conditions
		# If length is 0 or 1, there is only 1 permutation
        if n in [0, 1]:
            return [nums]
		
		# If length is 2, then there are only two permutations
		# Example: [1,2] and [2,1]
        if n == 2:
            return [nums, nums[::-1]]
			
        res = []
		# For every number in array, choose 1 number and permute the remaining
		# by calling permute recursively
        for i in range(n):
            permutations = self.permute(nums[:i] + nums[i+1:])
            for p in permutations:
                res.append([nums[i]] + p)
				
        return res