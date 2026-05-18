class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rocks = stones.copy()
        rocks.sort()
        while rocks:
            if len(rocks) == 1:
                return sum(rocks)
            y = rocks.pop()
            x = rocks.pop()
            # if x == y:
            #     continue
            if x < y:
                rocks.append(abs(y-x))
                rocks.sort()
        return 0