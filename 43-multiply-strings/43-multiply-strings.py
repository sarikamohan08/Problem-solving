class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = '0987654321'

        b =[0,9,8,7,6,5,4,3,2,1]

        nums = dict(zip(a,b))

        

        n1, n2 = 0, 0

        

        for n in range(len(num1)):

            n1 = (n1 + nums[num1[n]])*10 if n < len(num1)-1 else (n1 + nums[num1[n]])

        for n in range(len(num2)):

            n2 = (n2 + nums[num2[n]])*10 if n < len(num2)-1 else (n2 + nums[num2[n]])

            

        return str(n1*n2)