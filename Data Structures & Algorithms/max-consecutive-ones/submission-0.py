class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count_ones = 0
        left = 0
        for num in nums:
            if num == 0:
                maxi = max(maxi, count_ones)
                count_ones = 0
                continue
            count_ones += 1
        maxi = max(maxi, count_ones)
        return maxi