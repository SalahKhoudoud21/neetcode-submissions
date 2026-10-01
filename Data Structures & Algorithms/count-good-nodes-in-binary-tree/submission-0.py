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
            
            if node.val > maxNode:
                maxNode = node.val

            left = dfs(node.left, maxNode)
            right = dfs(node.right, maxNode)

            if node.val >= maxNode:
                return 1 + left + right
            
            return left + right
        
        return dfs(root, float('-inf'))
