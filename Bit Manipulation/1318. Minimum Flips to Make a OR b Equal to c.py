class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        common_bits = (a & b)
        different_bits = (a | b) ^ c
        return different_bits.bit_count() + (common_bits & different_bits).bit_count()
