class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        
        def backtracking(start, subset):
            result.append(subset.copy())
            
            for i in range(start, n):
                subset.append(nums[i]) # append
                backtracking(i + 1, subset) # explore
                subset.pop() # backtrack
            
            return 0
        backtracking(0, [])
        return result
            