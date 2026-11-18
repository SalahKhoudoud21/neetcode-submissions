import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, -num)
      

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = [] # temporary storage
        for _ in range(self.k-1):
            temp.append(heapq.heappop(self.heap))
        
        k_largest = self.heap[0]
        for num in temp:
            heapq.heappush(self.heap, num)
    
        return -k_largest
        
        
