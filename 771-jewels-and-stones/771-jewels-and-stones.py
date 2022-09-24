class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        list1=[]
        for letter in stones:
            list1.append(letter)
        print(list1)
        count=0
        for i in range(len(list1)):
            if(list1[i]in jewels):
                count+=1
        return count