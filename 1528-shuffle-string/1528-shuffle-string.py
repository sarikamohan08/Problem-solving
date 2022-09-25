class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
            new_s = ['']*len(indices)
            for i, index in enumerate(indices):
                new_s[index] = s[i]
            return ''.join(new_s)