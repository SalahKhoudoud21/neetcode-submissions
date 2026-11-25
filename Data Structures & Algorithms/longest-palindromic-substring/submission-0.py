class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_p = ''
        for i in range(n):
            # odd expansion
            l = i
            r = i
            sub_str1 = s[i]
            while True:
                if l < 0 or r >= n or s[l] != s[r]:
                    break
                
                if l != r:
                    sub_str1 = s[l] + sub_str1 + s[r]  
                l -= 1
                r += 1
            if len(sub_str1) > len(longest_p):
                longest_p = sub_str1
            # even expansion
            l = i
            r = i + 1
            sub_str2 = ''
            while True:
                if l < 0 or r >= n or s[l] != s[r]:
                    break
                
                sub_str2 = s[l] + sub_str2 + s[r]
                
                l -= 1
                r += 1
            
            if len(sub_str2) > len(longest_p):
                longest_p = sub_str2
            
        return longest_p



