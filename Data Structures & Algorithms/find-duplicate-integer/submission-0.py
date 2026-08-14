class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow_new = 0
        while slow != slow_new:
            slow = nums[slow]
            slow_new = nums[slow_new]
        return slow


        