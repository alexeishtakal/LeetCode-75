class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pl = [0] * len(nums)
        pr = [0] * len(nums)
        pl[0] = nums[0]
        pr[-1] = nums[-1]
        for i in range(1, len(nums)):
            pl[i] = pl[i - 1] + nums[i]
            pr[-i - 1] = pr[-i] + nums[-i - 1]
        for i in range(len(nums)):
            if pl[i] == pr[i]:
                return i

        return -1
