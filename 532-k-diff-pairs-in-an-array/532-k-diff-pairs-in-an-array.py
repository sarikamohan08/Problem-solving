class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        ans = 0
        for key in hashMap:
            if k == 0:
                if hashMap[key] > 1:
                    ans += 1
            else:
                if key + k in hashMap:
                    ans += 1
        return ans
        