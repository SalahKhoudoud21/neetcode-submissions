class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtracking(start, sumSoFar, lista):
            if sumSoFar == target:
                result.append(lista.copy())
                return 0
            
            if sumSoFar > target:
                return 0
            
            for i in range(start, n):
                sumSoFar += nums[i]
                lista += [nums[i]]
                backtracking(i, sumSoFar, lista)
                sumSoFar -= lista.pop() # backtracking
                
            return 0
        
        backtracking(0, 0, [])
        return result

