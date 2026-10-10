class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = {'+', 'C', 'D'}
        for operation in operations:
            if operation in ops:
                if operation == '+':
                    num1 = stack[-1]
                    num2 = stack[-2]
                    stack.append(num1 + num2)
                elif operation == 'C':
                    stack.pop()
                else:
                    stack.append(stack[-1] * 2)
            else:
                stack.append(int(operation))
        return sum(stack)

                
