from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicto = Counter(nums)
        return any(x > 1 for x in dicto.values())