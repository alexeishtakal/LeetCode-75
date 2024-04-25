class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        out = float(-9999)
        if k > 0:
            current = sum(nums[:k])
            print(f'init current {current}')
            out = float(current / k)
            for i in range(len(nums) - k):
                current = current - nums[i]
                current = current + nums[i + k]
                out = max(out, current / k)
            return (float(out))
        else:
            return float(nums[0])
