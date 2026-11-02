from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        que = deque([])

        for row in range(rows):
            for col in range(cols):
                entry = grid[row][col]
                if entry == 2:
                    que.append((row,col,0))
        
        elapsed_t = 0
        while que:
            r, c, t = que.popleft()
            elapsed_t = t
            neighbors = [(r+1,c), (r-1,c), (r, c+1), (r,c-1)]

            for neighbor in neighbors:
                # Checking invalid
                ro, co = neighbor
                
                if ro < 0 or co < 0 or ro >= rows or co >= cols or grid[ro][co] == 0:
                    continue
                
                if grid[ro][co] != 2: # grid can act as the visited
                    que.append((ro,co,t+1))
                    grid[ro][co] = 2 # becomes rotten
        
        for row in range(rows):
            for col in range(cols):
                entry = grid[row][col]
                if entry == 1:
                    return -1
        
        return elapsed_t