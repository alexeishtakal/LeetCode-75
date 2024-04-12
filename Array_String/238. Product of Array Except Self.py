class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        prefix = 1
        postfix = 1
        for i in range(0, len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer
