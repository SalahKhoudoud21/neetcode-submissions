import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x1, y1):
            return x1**2 + y1**2 # since x2,y2 is origin => (0,0)
        max_heap = []
        for x,y in points:
            distance_to_origin = euclidean_distance(x, y) # always positive
            if len(max_heap) == k:
                if -max_heap[0][0] > distance_to_origin:
                    heapq.heapreplace(max_heap, (-distance_to_origin, [x,y]))
            else:
                heapq.heappush(max_heap, (-distance_to_origin, [x,y]))
        out = []
        for _, coordinates in max_heap:
            out.append(coordinates)
        return out