class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        encoder = [0] * 26
        for char in s1:
            encoder[ord(char) - ord('a')] += 1
        
        n = len(s1)
        left = 0
        enc_s2 = [0] * 26
        for i, char in enumerate(s2):
            index = ord(char) - ord('a')
            enc_s2[index] += 1
            window_size = i - left + 1
            while window_size > n:
                enc_s2[ord(s2[left]) - ord('a')] -= 1
                left += 1
                window_size = i - left + 1
            if window_size == n:
                if enc_s2 == encoder:
                        return True
        return enc_s2 == encoder

                
                

            

        
        
