class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_p = ''
        start = 0
        max_len = 0 # length of longest palindrome
        for i in range(n):
            # odd expansion
            l = i
            r = i
            while True:
                if l < 0 or r >= n or s[l] != s[r]:
                    break
                
                if (r - l + 1) > (max_len):
                    max_len = r - l + 1
                    start = l
               
                l -= 1
                r += 1
    
            # even expansion
            l = i
            r = i + 1
            while True:
                if l < 0 or r >= n or s[l] != s[r]:
                    break
                
                if (r - l + 1) > (max_len):
                    max_len = r - l + 1
                    start = l
                
                l -= 1
                r += 1
            
        return s[start:start+max_len]



