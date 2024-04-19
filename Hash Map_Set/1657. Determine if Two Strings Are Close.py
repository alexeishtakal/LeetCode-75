class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        sorted_values_word1 = sorted(freq1.values())
        sorted_values_word2 = sorted(freq2.values())

        keys_match = set(freq1.keys()) == set(freq2.keys())

        return sorted_values_word1 == sorted_values_word2 and keys_match
