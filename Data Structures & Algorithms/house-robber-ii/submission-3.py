class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Base cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        
        # Last house excluded
        dp1 = [0] * n # Represents max amount of money from 0 up to house i
        dp1[0] = nums[0]
        dp1[1] = max(nums[1], nums[0])
        # First house excluded
        dp2 = [0] * n
        dp2[1] = nums[1]

        for i in range(2,n):
            if i == (n-1):
                dp1[i] = dp1[i-1]
            else:
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
            
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
        
        return max(dp2[-1], dp1[-1])


        