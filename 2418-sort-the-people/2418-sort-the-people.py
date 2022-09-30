class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        D = zip(heights,names)
        D = list(D)
        D.sort()
        ans = []
        for i in D:
            ans.append(i[1])

        return ans[::-1]