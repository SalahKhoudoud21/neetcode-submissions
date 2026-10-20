class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        n = len(nums)
        def backtracking(start, subset):
            subsets.append(subset.copy())

            for i in range(start, n):
                if i > start:
                    if nums[i] == nums[i-1]:
                        continue
                    
                subset.append(nums[i])
                backtracking(i+1, subset)
                subset.pop()
            return
        
        backtracking(0, [])
        return subsets
