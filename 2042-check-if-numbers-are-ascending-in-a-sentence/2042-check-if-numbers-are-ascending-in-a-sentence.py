class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=s.split() #break the string into list
        n = 0 #to store the previous number
        for i in l:
            if i.isdigit():
                if int(i) <= n: #if at any point the previous number is greater, return False
                    return False
                n = int(i) #update the previous number
        return True