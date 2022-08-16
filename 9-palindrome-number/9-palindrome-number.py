class Solution:
    def isPalindrome(self, x: int) -> bool:
            start = x
            if x<0:
                return False;
            elif x==0:
                return True;
            result = 0;
            while x>0:
                target = x % 10;
                result = result*10 + target;
                x = x // 10;
            return result==start
