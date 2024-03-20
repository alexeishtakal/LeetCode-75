class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        total_sum = 0
        heap = []
        merged = [[y, x] for y, x in sorted(zip(nums2, nums1), reverse=True)]
        for num2, num1 in merged:
            if len(heap) == k:
                total_sum -= heapq.heappop(heap)
            total_sum += num1
            heapq.heappush(heap, num1)
            if len(heap) == k:
                result = max(result, total_sum * num2)
        return result

