class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort(reverse = True)
            first = stones.pop(0)
            second = stones.pop(0)
            if first == second:
                continue
            else:
                stones.append(first-second)
        if stones:
            return stones[0]
        else:
            return 0