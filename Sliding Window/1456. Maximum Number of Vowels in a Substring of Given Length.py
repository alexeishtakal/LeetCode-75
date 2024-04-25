class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_vowels = 0
        current_vowels = 0
        for i, v in enumerate(s):
            if i>=k:
                if s[i-k] in vowels:
                    current_vowels-=1
            if s[i] in vowels:
                current_vowels+=1
            max_vowels = max(max_vowels, current_vowels)
        return max_vowels