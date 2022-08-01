class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
       
        freq=[0]*100000
        for i in range(len(nums)):
            freq[nums[i]]+=1

        for i in range(100000):
            if(freq[i]>0):
                print(i,freq[i])

        l=[]
        for i in range(100000):
            if(freq[i]>1):
                l.append(i)
                continue
                
        return l