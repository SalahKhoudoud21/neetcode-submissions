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
            for _ in range(len_que-1): # keep adding until reach the last node because thats the node of interest
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)    
            
            node_of_interest = que.popleft()
            right_side.append(node_of_interest.val)
            
            if node_of_interest.left:
                que.append(node_of_interest.left)
            if node_of_interest.right:
                que.append(node_of_interest.right)
        
        return right_side
            

                