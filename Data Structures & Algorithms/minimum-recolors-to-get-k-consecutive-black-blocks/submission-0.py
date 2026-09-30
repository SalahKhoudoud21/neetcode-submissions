class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black_boxes = 0
        left = 0
        switched = float("inf")
        for i, block in enumerate(blocks):
            if block == 'B':
                black_boxes += 1
            
            if i >= k - 1:
                switched = min(switched, (i - left + 1) - black_boxes)
                if blocks[left] == 'B':
                    black_boxes -= 1
                left += 1
        return switched


