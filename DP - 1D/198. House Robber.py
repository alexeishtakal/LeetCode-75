class Solution:
    def __init__(self):
        self.cache = {}

    def rec(self, nums, start):
        if start >= len(nums):
            return 0
        if start in self.cache:
            return self.cache[start]

        self.cache[start] = nums[start] + max(self.rec(nums, start + 2), self.rec(nums, start + 3))
        return self.cache[start]

    def rob(self, nums: List[int]) -> int:
        # return max(self.rec(nums, 0), self.rec(nums, 1))

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]




