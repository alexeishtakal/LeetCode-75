class Solution:
    def recursion(self, text1, text2, i, j):
        if i==len(text1) or j==len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + self.recursion(text1, text2, i+1, j+1)
        else:
            return max(self.recursion(text1, text2, i+1, j), self.recursion(text1, text2, i, j+1))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #return self.recursion(text1, text2, 0, 0)
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)][len(text2)]
