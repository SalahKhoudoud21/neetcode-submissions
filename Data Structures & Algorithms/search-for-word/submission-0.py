class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        n = len(word)
        visited = set()
        def backtracking(r, c, i):
            if i == n:
                return True
            
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or ((r,c) in visited) or (board[r][c] != word[i]): # out of bounds, or visited the entry already or doesnt correspond to right character
                return False
            
            visited.add((r,c))
            result = backtracking(r+1, c, i+1) or backtracking(r-1,c,i+1) or backtracking(r, c+1, i+1) or backtracking(r, c-1, i+1)
            visited.remove((r,c))
            return result
        
        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0): return True
        
        return False
            

