class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        dic={0:-1}
        s=0
        for i in range(n):
            s=(s+nums[i])%k
            if s not in dic:
                dic[s]=i
                #print(dic)
            else:
                #print(i-dic[s])
                if(i-dic[s]>1):
                    return True
        return False
