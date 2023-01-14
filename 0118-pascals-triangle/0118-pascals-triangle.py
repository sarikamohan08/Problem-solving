class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        num_per_level = 2
        for i in range(numRows - 1):
            temp = [1] * num_per_level
            for j in range(len(res[-1]) - 1):
                temp[j + 1] = res[-1][j] + res[-1][j + 1]
            num_per_level += 1
            res.append(temp)
        return res