class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        correct = n * (n+1)//2
        return correct - sum(nums)