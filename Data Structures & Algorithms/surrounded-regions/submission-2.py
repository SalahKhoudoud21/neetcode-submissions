class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows, cols = len(board), len(board[0])
        
        for col in range(cols):
            if board[0][col] == 'O' and (0, col) not in visited:
                visited.add((0,col))
            
            if board[-1][col] == 'O' and (rows-1, col) not in visited:
                visited.add((rows-1, col))
            
        
        for row in range(rows):
            if board[row][0] == 'O' and (row, 0) not in visited:
                visited.add((row, 0))
            
            if board[row][-1] == 'O' and (row, col-1) not in visited:
                visited.add((row, cols-1))
        
        stack = list(visited)
        # DFS starts to see how far this edge O can extend because those Os cant be encircled
        while stack:
            r, c = stack.pop()
        
            neighbors = [(r+1, c) , (r-1, c), (r, c+1), (r, c-1)]
            
            for neighbor in neighbors:
                ro, co = neighbor
                if ro < 0 or co < 0 or ro >= rows or co >= cols or (ro, co) in visited:
                    continue
                
                item = board[ro][co]
                
                if item =='O':
                    visited.add((ro,co))
                    stack.append((ro,co))

        # visited now has all O locations that arent surrounded
        for row in range(1, rows-1):
            for col in range(1, cols -1):
                if (row,col) not in visited:
                    board[row][col] = 'X'




