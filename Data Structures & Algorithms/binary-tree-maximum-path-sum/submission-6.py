# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float('-inf')
        def dfs(node):
            nonlocal maxPath

            if not node:
                return 0
            
            curr = node.val

            left = dfs(node.left)
            right = dfs(node.right)

            maxPath = max(maxPath, left + curr + right, curr + left, curr + right, curr)

            return max(curr + max(left, right), curr)
        
        dfs(root)
        return maxPath



            
            