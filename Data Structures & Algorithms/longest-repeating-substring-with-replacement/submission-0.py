from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxi = 0
        dicto = defaultdict(int)
        for i, char in enumerate(s):
            window_size = i - left + 1
            dicto[char] += 1
            majority = max(dicto.values())
            replacements = window_size - majority
            while replacements > k:
                dicto[s[left]] -= 1
                left += 1
                window_size = i - left + 1
                majority = max(dicto.values())
                replacements = window_size - majority
            maxi = max(maxi, window_size)
        return maxi

        
            

            