class Solution:
    def backtrack(self, num, stack, target):
        if len(stack) == self.k:
            if target == 0:
                self.res.append(stack)
            return

        for x in range(num + 1, 10):
            if x <= target:
                self.backtrack(x, stack + [x], target - x)
            else:
                return

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.k = k
        self.res = []
        self.backtrack(0, [], n)
        return self.res