class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = '.' * n # empty row
        combinations = []
        
        def backtracking(combination, blocked_cols, pos_diags, neg_diags):
            if len(combination) == n:
                combinations.append(combination.copy())
            
            r = len(combination) # current row
            for c in range(n): # columns
                if c not in blocked_cols and r + c not in pos_diags and r - c not in neg_diags:        
                    blocked_cols.add(c)
                    pos_diags.add(r+c)
                    neg_diags.add(r-c)
                    combination.append(row[:c] + 'Q' + row[c+1:])
                    backtracking(combination, blocked_cols, pos_diags, neg_diags)
                    combination.pop()
                    blocked_cols.remove(c)
                    pos_diags.remove(r+c)
                    neg_diags.remove(r-c)
            
            return
        
        backtracking([], set(), set(), set())
        return combinations
                                

                    
                            


            
            
                