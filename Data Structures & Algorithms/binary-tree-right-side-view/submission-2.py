# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque([root])
        right_side = []
        while que:
            len_que = len(que)
            for _ in range(len_que-1):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)    
            node = que.popleft()
            right_side.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return right_side
            

                