class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        s = len(nums)
        even = nums[0:s:2]
        even.sort()
        odd = nums[1:s:2]
        odd.sort(reverse=True)
        l=[]
        for i in range(s):
            if(i%2==0):
                l.append(even[i//2])
            else:
                l.append(odd[i//2])
        return l