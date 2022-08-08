class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for (start,end) in intervals[1:]:
            if ans[-1][1] < start:
                ans.append([start,end])
            else:
                ans[-1][1] = max(ans[-1][1], end)
                
        return ans