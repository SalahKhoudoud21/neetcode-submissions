
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_entry = []
        atlantic_entry = []
        res = []

        for col in range(cols):
            pacific_entry.append((0,col))
            atlantic_entry.append((rows-1, col))
            
        
        for row in range(rows):
            pacific_entry.append((row,0))
            atlantic_entry.append((row, cols-1))
        
        visited_pacific = set(pacific_entry) # represents entries that can reach pacific
        # BFS to find which entries can reach pacific
        # start bfs from each boundary point
        que = deque(list(visited_pacific))
        while que:
            r, c = que.popleft()
            curr_h = heights[r][c]
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]
            for neighbor in neighbors:
                ro, co = neighbor
                
                if ro < 0 or co < 0 or co >= cols or ro >= rows or neighbor in visited_pacific:
                    continue
                    
                h_neighb = heights[ro][co]
                
                if curr_h <= h_neighb: # we can propagate
                    visited_pacific.add(neighbor)
                    que.append(neighbor)
        
        visited_atlantic = set(atlantic_entry)
        que = deque(list(visited_atlantic))
        print(que)
        while que:
            r, c = que.popleft()
            
            if (r,c) in visited_pacific:
                print('hi')
                res.append(list((r,c)))
                
            curr_h = heights[r][c]
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]
            
            for neighbor in neighbors:
                ro, co = neighbor
                
                if ro < 0 or co < 0 or co >= cols or ro >= rows or neighbor in visited_atlantic:
                    continue
                    
                h_neighb = heights[ro][co]
                
                if curr_h <= h_neighb: # we can propagate
                    visited_atlantic.add(neighbor)
                    que.append(neighbor)
        
        return res
                    
                        






        
        

       
