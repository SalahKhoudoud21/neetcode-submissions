# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        
        def dfs(node1, node2):
            nonlocal same
            if not node1 and not node2:
                return
            
            elif not node1 or not node2:
                same = False
                return
            
            if node1.val != node2.val:
                same = False
                return
            
            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

        dfs(p,q)
        return same
            
