class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        islands = 0
        for r in range(rows):
            for c in range(cols):
                entry = grid[r][c]
                if entry == '1' and (r,c) not in visited:
                    islands += 1
                    stack = [(r,c)]
                    while stack:
                        ro,co = stack.pop()
                        if ro < 0 or co < 0 or ro >= rows or co >= cols:
                            continue
                        
                        if (ro, co) not in visited and grid[ro][co] == '1':
                            visited.add((ro,co))
                            neighbors = [(ro+1, co), (ro-1, co), (ro, co+1), (ro,co-1)]
                            for neighbor in neighbors:
                                if neighbor not in visited:
                                    stack.append(neighbor)
        return islands
                            
                        

                            


