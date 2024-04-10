class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        current_divisor=""
        for i in range(min(len(str1), len(str2))):
            divisor=str1[:i+1]
            current_max_d1 = divisor * int(len(str1)/len(divisor))
            current_max_d2 = divisor * int(len(str2)/len(divisor))
            if current_max_d1 == str1 and current_max_d2 == str2:
                current_divisor = divisor
        return current_divisor