class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """time limit exceeded
        n=len(nums)
        arr=nums
        freq=[0]*100000000
        for i in range(n):
            freq[arr[i]]+=1

        for i in range(100000000):
            if(freq[i]>0):
                print(i,freq[i])

        flag=0
        for i in range(100000000):
            if(freq[i]>1):
                flag=1
                break
        if(flag==1):
            return True
        else:
            return False
        """ 
        #python inbuilt datastructure
        
        return True if len(set(nums)) < len(nums) else False