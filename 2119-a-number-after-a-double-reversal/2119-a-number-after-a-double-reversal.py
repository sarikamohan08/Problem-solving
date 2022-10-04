class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if len(str(num)) > 1 and str(num)[-1] == "0":
            return False
        else:
	        return True