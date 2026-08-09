class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i-1])
        
        for i in range(n-2, -1,-1):
            max_right[i] = max(height[i], max_right[i+1])
        water = 0
        for i in range(n):
            water += min(max_right[i], max_left[i]) - height[i]
        return water
        
