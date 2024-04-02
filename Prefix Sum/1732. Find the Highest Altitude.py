class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        import array
        p = array.array('i', [0] * (len(gain) + 1))
        p[0] = gain[0]
        for k in range(1, len(gain)):
            p[k] = p[k - 1] + gain[k]
        max_alt = max(p)
        return max_alt
