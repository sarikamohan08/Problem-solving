class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        mp="0123456789abcdef"
        ans=""
        for i in range(8):
            ans=mp[num%16]+ans
            num=num//16
        return ans.lstrip('0')