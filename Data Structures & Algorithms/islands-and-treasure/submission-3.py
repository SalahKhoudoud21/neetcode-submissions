from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure_locs = []
        rows, cols = len(grid), len(grid[0])
        
        # find the treasure locations
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    treasure_locs.append((row,col))
        
        que = deque(treasure_locs)
        while que:
            r,c = que.popleft()
            neighbors = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            
            for ro, co in neighbors:
                if ro < 0 or co < 0 or ro >= rows or co >= cols:
                    continue
                entry = grid[ro][co]
                if entry == 2147483647:
                    grid[ro][co] = grid[r][c] + 1
                    que.append((ro,co))
        