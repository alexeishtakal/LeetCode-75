class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = 2147483648
        b = 2147483649
        for i in range(len(nums)):
            if a >= nums[i]:
                a = nums[i]
            elif b >= nums[i]:
                b = nums[i]
            else:
                if a < b and b < nums[i]:
                    return True
        return False
