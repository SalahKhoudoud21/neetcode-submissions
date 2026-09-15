import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # remember that heapq.heappop() pops heap[0] unlike regular pop() which pops last element
        heap = []
        maxi = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-1*nums[i], i))
            
            if i >= k - 1:
                while heap[0][1] <= i - k: # outside the window we remove
                    heapq.heappop(heap)
                
                val, index = heap[0]
                maxi.append(-1*val)
        return maxi
            

