class Solution:
    # def dp(self, cost, n):
    #     if n < 2:
    #         return cost[n]
    #     return cost[n] + min(self.dp(cost, n - 1), self.dp(cost, n - 2))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # length = len(cost)
        # return min(self.dp(cost, length - 1), self.dp(cost, length - 2))

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])
