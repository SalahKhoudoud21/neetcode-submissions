class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mini = float('inf')
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            
            middle = left + ((right - left)//2)
            if nums[left] <= nums[middle]:
                left = middle + 1
            
            else:
                right = middle
        return 0