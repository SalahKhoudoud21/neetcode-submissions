# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxNode):
            if not node:
                return 0
            
            current = 1 if node.val >= maxNode else 0
            
            maxNode = max(maxNode, node.val)

            left = dfs(node.left, maxNode)
            right = dfs(node.right, maxNode)
            
            return current + left + right
        
        return dfs(root, float('-inf'))
