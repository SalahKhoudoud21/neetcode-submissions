class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        unique = set()
        left = 0
        maxi = 0
        for i, char in enumerate(s):
            if char in unique:
                while True:
                    if s[left] == char:
                        left += 1
                        break
                    unique.remove(s[left])
                    left += 1
                
            else:
                maxi = max(maxi, i - left + 1)
                unique.add(char)
        maxi = max(maxi, i - left + 1)
        return maxi
            
            