class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        end_i=0
        for i in range(0, min(len(word1), len(word2)), 1):
            result+=word1[i]
            result+=word2[i]
            end_i=i+1
        result+=word1[end_i:]
        result+=word2[end_i:]
        return result
