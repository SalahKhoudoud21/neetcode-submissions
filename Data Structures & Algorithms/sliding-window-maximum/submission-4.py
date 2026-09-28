import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        maximums = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                maximums.append(-1*heap[0][0])
        return maximums