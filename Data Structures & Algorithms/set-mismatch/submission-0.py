from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        sequence = set(range(1, n+1))
        out = []
        out.append(next(key for key in freq if freq[key] > 1))
        for num in sequence:
            if num not in freq:
                return out + [num]
        return 0
        