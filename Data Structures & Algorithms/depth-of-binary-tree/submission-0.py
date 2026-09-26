# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = deque([root])
        longest = 0
        while que:
            len_que = len(que)
            for _ in range(len_que):
                node = que.popleft()
                if node:
                    que.append(node.left) if node.left else None
                    que.append(node.right) if node.right else None
            longest += 1
        return longest
