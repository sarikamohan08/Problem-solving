class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=[]
        for i in nums:
            if i%3==0 and i%2==0:
                s.append(i)
        if len(s)==0:
            return 0
        avg=sum(s)//len(s)
        return avg