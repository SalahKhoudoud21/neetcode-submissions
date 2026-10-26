class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_options = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz',
        }
        combinations = []
        n = len(digits)
        def backtracking(start, combination):
            if len(combination) == n:
                combinations.append(combination)
                return
            
            for i in range(start, n):
                letters = digit_options[digits[i]]
                for letter in letters:
                    combination += letter
                    backtracking(i+1, combination)
                    combination = combination[:-1]
            return
        backtracking(0, "")
        return combinations
                    