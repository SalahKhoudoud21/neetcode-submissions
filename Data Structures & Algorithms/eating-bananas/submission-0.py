class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles) # - > # len(piles) hours
        lower_bound = 1 # eating one banana per hour
        best_so_far = upper_bound
        while lower_bound <= upper_bound:
            middle_k = lower_bound + ((upper_bound - lower_bound)//2)
            hours_needed = 0
            
            for pile in piles:
                hours_needed += math.ceil(pile/middle_k) 

            if hours_needed <= h:
                best_so_far = middle_k
                
                upper_bound = middle_k - 1
            else:
                lower_bound = middle_k + 1
        return best_so_far
            
            
            



        

