from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        que = deque([])
        visited = set()
        
        for row in range(rows):
            for col in range(cols):
                entry = grid[row][col]
                if entry == 0: # add to que
                    que.append((row,col))
                    visited.add((row,col))
        
        while que:
            r, c = que.popleft()
            
            neighbors = [(r+1, c), (r-1,c), (r, c+1), (r, c-1)]
            for neighbor in neighbors:
                ro, co = neighbor
                if ro < 0 or co < 0 or ro >= rows or co >= cols or grid[ro][co] == -1:
                    continue
                
                if neighbor not in visited:
                    grid[ro][co] = grid[r][c] + 1
                    visited.add((ro,co))
                    que.append(neighbor)
               
                    
        
            
                        
                    
                                
                                

                                


