class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # if even median is middle 2 number / 2
        # if odd median is just middle number

        S, B = nums1, nums2
        if len(B) < len(S):
            S, B = B, S
        
        total = len(S) + len(B)
        left_half = total // 2
        
        l, r = 0, len(S) - 1
        while True:
            
            
            i = l + ((r - l)//2)
            j = left_half - i - 2 # because - 1 from each len so -1 * 2

            # Big and Small are for the sizes of arrays nums1 and nums2

            small_left = S[i] if i >= 0 else float("-infinity")
            small_right = S[i+1] if i + 1 < len(S) else float("infinity")

            big_left = B[j] if j >= 0 else float("-infinity")
            big_right = B[j+1] if j + 1 < len(B) else float("infinity")

            # good partition
            if small_left <= big_right and big_left <= small_right:
                median = min(small_right, big_right) if total % 2 != 0 else (max(small_left, big_left) + min(small_right, big_right))/2
                return median
            
            elif small_left > big_right:
                r = i - 1
            
            else: # big_left > small_right
                l = i + 1
        
        

