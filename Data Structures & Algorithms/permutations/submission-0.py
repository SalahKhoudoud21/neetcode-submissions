class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        used = [False] * n
        def backtracking(permutation, used):
            if len(permutation) == n:
                permutations.append(permutation.copy())
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    permutation.append(nums[i])
                    backtracking(permutation, used)
                    used[i] = False
                    permutation.pop()
            return
            
        
        backtracking([], used)
        return permutations
