import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # identical tasks must be separated by at least n CPU cycles
        freq = Counter(tasks)
        heap = []
       
        for val in freq.values():
            heapq.heappush_max(heap, val)
        
        time = 0
        que = deque([])
        while True:
            if heap:
                task = heapq.heappop_max(heap)
                task -= 1
                time += 1
                if task > 0:
                    que.append((task, time+n)) # time + n is time until ready to use again
            
            elif que: # idle no tasks left in heap
               time += 1    
            
            if que and que[0][1] == time: # ready to append to heap again
                task, _ = que.popleft()
                heapq.heappush_max(heap, task)

            if not heap and not que: # no tasks left at all
                return time




        
        
        