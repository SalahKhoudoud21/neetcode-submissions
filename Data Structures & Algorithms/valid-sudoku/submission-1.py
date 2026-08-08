class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(1) Space
        # O(1) Time
        
        rows_valid = [[False] * 9 for _ in range(9)]
        cols_valid = [[False] * 9 for _ in range(9)]
        box_valid = [[False] * 9 for _ in range(9)]

        for row in range(9):
            for col in range(9):
                entry = board[row][col]
                if entry == ".": # we skip
                    continue
                else:
                    digit_idx = int(entry) - 1

                    box_idx = row//3 * 3 + col//3

                    if rows_valid[row][digit_idx] or cols_valid[col][digit_idx] or box_valid[box_idx][digit_idx]:
                        return False
                
                rows_valid[row][digit_idx] = True
                cols_valid[col][digit_idx] = True
                box_valid[box_idx][digit_idx] = True
        return True

