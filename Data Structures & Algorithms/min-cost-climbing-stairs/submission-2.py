class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) # number of steps
        if n == 1:
            return cost[0]
        
        dp1 = [0] * (n + 1) # start at 0
        dp2 = [0] * (n + 1) # start at 1
        dp1[1] = cost[0]
        dp2[2] = cost[1]
        for i in range(2, n+1):
            dp1[i] = min(dp1[i-1] + cost[i-1], dp1[i-2] + cost[i-2])
        
        for i in range(3, n+1):
            dp2[i] = min(dp2[i-1] + cost[i-1], dp2[i-2] + cost[i-2])

        return min(dp1[-1], dp2[-1])

