class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr=set(nums)
        a,n=[],len(nums)
        for i in range(1,n+1):
            if i not in arr:
                a.append(i)
        return a