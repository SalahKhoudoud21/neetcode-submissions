from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        nums_updated = list(frequency.keys())
        nums_updated.sort(key=frequency.get, reverse=True)
        return nums_updated[:k]