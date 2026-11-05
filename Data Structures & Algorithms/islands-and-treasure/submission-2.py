from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        treasures = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    treasures.append((row,col))
        
        que = deque(treasures)
        visited = set(treasures)
        while que:
            r, c = que.popleft()
            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for neighbor in neighbors:
                ro, co = neighbor
                if ro < 0 or co < 0 or co >= cols or ro >= rows or (ro, co) in visited:
                    continue
                
                entry = grid[ro][co]
                
                if entry != -1:
                    que.append((ro,co))
                    visited.add((ro,co))
                    grid[ro][co] = grid[r][c] + 1
        



