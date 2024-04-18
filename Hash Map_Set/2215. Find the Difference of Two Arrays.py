class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set(nums1)
        ans2 = set(nums2)
        return [list(ans1-ans2), list(ans2-ans1)]