class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        xor_count = defaultdict(int)
        xor_count[0] += 1 
        xor = count = 0 
        for item in nums :
            xor ^= item 
            if xor in xor_count :
                count += xor_count[xor]
            
            xor_count[xor] += 1 
            
        return count 