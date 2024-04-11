class Solution:
    # -------
    # |t1|t3|
    # |t2|t4|
    # -------
    def make_state(self, t1, t2):
        if not t1 and not t2:
            return 0
        if t1 and not t2:
            return 1
        if not t1 and t2:
            return 2
        return 3

    def place(self, dp, i, t1, t2):
        if i == self.n:
            return 1
        state = self.make_state(t1, t2)
        if dp[i][state]:
            return dp[i][state]
        t3 = i + 1 < self.n
        t4 = i + 1 < self.n
        count = 0
        if t1 and t2:
            count += self.place(dp, i + 1, True, True)
        if not t1 and not t2:
            count += self.place(dp, i + 1, True, True)

        if t1 and t2 and t3 and t4:
            count += self.place(dp, i + 1, False, False)

        if t1 and t2 and t3:
            count += self.place(dp, i + 1, False, True)
        if t1 and t2 and t3:
            count += self.place(dp, i + 1, True, False)

        if t1 and not t2 and t3 and t4:
            count += self.place(dp, i + 1, False, False)
        if not t1 and t2 and t3 and t4:
            count += self.place(dp, i + 1, False, False)

        if t1 and not t2 and t3:
            count += self.place(dp, i + 1, False, True)
        if not t1 and t2 and t4:
            count += self.place(dp, i + 1, True, False)
        dp[i][state] = count % 1000000007
        return dp[i][state]

    def numTilings(self, n: int) -> int:
        self.n = n
        dp = [[None] * 4 for _ in range(n + 1)]
        result = self.place(dp, 0, True, True)
        return result
