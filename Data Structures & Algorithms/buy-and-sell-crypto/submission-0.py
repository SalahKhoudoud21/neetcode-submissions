class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for i, price in enumerate(prices):
            while prices[left] > price:
                if left == len(prices):
                    break
                left += 1
            max_profit = max(max_profit, price - prices[left])
        return max_profit
            
            