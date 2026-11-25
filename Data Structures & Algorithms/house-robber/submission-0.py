class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) # number of houses
        
        if n == 1: # base case
            return nums[0]
        
        if n == 2: # base case
            return max(nums[0], nums[1])
        
        dp = [0] * n # dp[i] represents max amount of money we can make from 0 up to i
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]
        

        
