class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxi = float('-inf')
        while left < right:
            if heights[left] > heights[right]:
                aire = heights[right] * (right - left)
                right -= 1
            elif heights[left] < heights[right]:
                aire = heights[left] * (right - left)
                left += 1
            else:
                aire = heights[left] * (right - left)
                left += 1
                right -= 1
            maxi = max(maxi, aire)
        return maxi
