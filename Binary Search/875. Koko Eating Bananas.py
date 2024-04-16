class Solution:

    def is_ok(self, piles, cnt, h):
        return sum(ceil(i / cnt) for i in piles) <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            if self.is_ok(piles, m, h):
                r = m
            else:
                l = m + 1

        return l
