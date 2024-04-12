class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        current_vowels = []
        for c in s:
            if c in vowels:
                current_vowels+=c
        v_i=-1
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = current_vowels[v_i]
                v_i-=1
        return "".join(s)