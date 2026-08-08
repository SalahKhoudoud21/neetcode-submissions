class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}
        for i, num in enumerate(nums):
            if target - num in dicto:
                return sorted([i,dicto[target-num]])
            else:
                dicto[num] = i
        return 0