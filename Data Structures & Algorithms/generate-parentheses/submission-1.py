class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        choices = ['(', ')']
        parentheses = []
        def backtracking(paran, left, right):
            if right > left or left > n or right > n:
                return
            
            if right + left == 2*n:
                parentheses.append(paran)
                return
            
            for choice in choices:
                paran += choice
                left += 1 if choice == '(' else 0
                right += 1 if choice ==')' else 0
                backtracking(paran, left, right)
                par = paran[-1]
                left -= 1 if par == '(' else 0
                right -= 1 if par == ')' else 0
                paran = paran[:-1]
            return
        
        backtracking('', 0, 0)
        return parentheses

                
