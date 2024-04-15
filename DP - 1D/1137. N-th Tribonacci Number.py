class Solution:
    # def rec(self, n):
    #     if n == 0:
    #         return 0
    #     if n == 1 or n == 2:
    #         return 1
    #     return self.rec(n - 1) + self.rec(n - 2) + self.rec(n - 3)

    def tribonacci(self, n: int) -> int:
        #return self.rec(n)
        tri = []
        tri.append(0)
        tri.append(1)
        tri.append(1)
        for i in range(3, n + 1):
            tri.append(tri[i - 1] + tri[i - 2] + tri[i - 3])
        return tri[n]
