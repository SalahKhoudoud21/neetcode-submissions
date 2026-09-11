class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # O(n + t) time
        # O(1) Space (Constant array sizes, and used variables)
        enc_t = [0] * 52
        required = 0
        for char in t:
            index = ord(char) - ord('a') if char.islower() else (ord(char) - ord('A')) + 26
            if enc_t[index] == 0:
                required += 1
            enc_t[index] += 1
        
        enc_s = [0] * 52
        left = 0
        formed = 0
        mini = float('inf')
        leftmost = 0
        rightmost = 0

        for i,char in enumerate(s):
            index = ord(char) - ord('a') if char.islower() else (ord(char) - ord('A')) + 26
            enc_s[index] += 1 if enc_t[index] != 0 else 0
            
            if enc_t[index] != 0 and enc_s[index] == enc_t[index]:
                formed += 1
            
            while formed == required:
                window_size = i - left + 1
                
                if window_size < mini:
                    mini = window_size
                    leftmost = left
                    rightmost = i
                cha = s[left]
                ind = ord(cha) - ord('a') if cha.islower() else (ord(cha) - ord('A')) + 26
                
                if enc_s[ind] != 0:
                    enc_s[ind] -= 1
                    if enc_s[ind] < enc_t[ind]:
                        formed -= 1
                left += 1
        
        if mini == float('inf'): # t wasnt found in s
            return ""
        
        return s[leftmost:rightmost+1] # t was found in s
            