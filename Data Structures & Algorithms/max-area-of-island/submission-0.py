class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                entry = grid[i][j]
                if entry == 1 and (i,j) not in visited:
                    # we start dfs
                    area = 0
                    stack = [(i,j)]
                    
                    while stack:
                        r, c = stack.pop()
                        if not (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited):
                            val = grid[r][c]
                            if val == 1:
                                visited.add((r,c))
                                area += 1
                                neighbors = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
                                for neighbor in neighbors:
                                    if neighbor not in visited:
                                        stack.append(neighbor)
                    maxArea = max(area, maxArea)
        
        return maxArea