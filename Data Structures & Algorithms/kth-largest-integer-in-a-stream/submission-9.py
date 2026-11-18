import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            if len(self.heap) == k:
                if self.heap[0] < num: 
                    heapq.heappop(self.heap) # get rid of smallest element to put a larger one in
                else:
                    continue
            heapq.heappush(self.heap,num)
        # by the end the heap should contain the k largest elements and heap[0] is smallest out of them
      

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        
        if self.heap[0] < val: # not k largest anymore
            # heapq.heappushpop(self.heap, val) less optimized cause still have to compare
            
            # optimization since we know that self.heap[0] is smallest and needs to be replaced
            heapq.heapreplace(self.heap, val) # replace smallest item with val
        
        return self.heap[0]
        
        
