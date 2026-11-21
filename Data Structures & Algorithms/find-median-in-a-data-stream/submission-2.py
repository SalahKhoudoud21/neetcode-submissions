# I will use the two heap approach
import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush_max(self.max_heap, num)
        
        elif num <= self.max_heap[0]:
            if len(self.max_heap) - len(self.min_heap) < 1:
                heapq.heappush_max(self.max_heap, num)
            
            else:
                maxi = self.max_heap[0]
                heapq.heapreplace_max(self.max_heap, num)
                heapq.heappush(self.min_heap, maxi)
        else:
            # we want to force the max_heap to contain extra elements always
            if len(self.min_heap) - len(self.max_heap) < 0:
               heapq.heappush(self.min_heap, num)
            
            else:
                if num > self.min_heap[0]:
                    mini = self.min_heap[0]
                    heapq.heapreplace(self.min_heap, num)
                    heapq.heappush_max(self.max_heap, mini)
                else:
                    heapq.heappush_max(self.max_heap, num)
    
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] + self.min_heap[0])/2
        return self.max_heap[0]
        
        