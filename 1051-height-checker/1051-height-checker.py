class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = sorted(heights)
        ct = 0
        for i in range(len(heights)):
            if res[i]!=heights[i]:
                ct+=1
        return ct