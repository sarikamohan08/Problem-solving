class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1, index2 = 0, len(numbers)-1
        while index1 < index2:
            curSum = numbers[index1] + numbers[index2]
            if curSum == target:
                break
            elif curSum < target:
                index1 += 1
            else:
                index2 -= 1
                
        
        return [index1+1, index2+1]