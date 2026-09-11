class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_of_interest = 0
        for i, row in enumerate(matrix):
            if row[-1] >= target:
                if row[-1] == target:
                    return True
                row_of_interest = i
                break
        
        left = 0
        right = len(matrix[row_of_interest]) - 1
        row = matrix[row_of_interest]
        while left <= right:
            middle = left + ((right - left) // 2)

            if row[middle] == target:
                return True
            
            if row[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False
