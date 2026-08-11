class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack_differences = [0] * n
        stack_indices = [0]
        for i in range(1, n):
            temp = temperatures[i]
            while stack_indices and temp > temperatures[stack_indices[-1]]:
                index = stack_indices.pop()
                stack_differences[index] = i - index
            stack_indices.append(i)
        return stack_differences