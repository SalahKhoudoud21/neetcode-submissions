class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1
        
        dp = [0] * len(s) # dp[i] number of valid ways to decode substring from 0 to i
        dp[0] = 1
        dp[1] += 1 if s[1] != '0' else 0
        dp[1] += 1 if int(s[0] + s[1]) < 27 else 0
        for i in range(2, len(s)):
            dp[i] += dp[i-1] if s[i] != '0' else 0
            dp[i] += dp[i-2] if int(s[i-1] + s[i]) < 27 and s[i-1] != '0' else 0
        return dp[-1]