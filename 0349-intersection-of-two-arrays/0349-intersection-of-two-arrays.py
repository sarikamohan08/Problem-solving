class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
       
        for i in range(len(nums2)):
            if(nums2[i] in nums1):
                l.append(nums2[i])
        
        return set(l)