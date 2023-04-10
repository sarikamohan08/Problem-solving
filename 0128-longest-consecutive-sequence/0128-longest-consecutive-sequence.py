class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        print(nums)
        for val in nums:
            #print(val)
            if val - 1 not in nums:
                print(val-1)
                count = val
                #print(count)
                while count in nums:
                    count += 1
                print(count)
                print(count-val)
                result = max(result, count - val)
                print(result)
        return result