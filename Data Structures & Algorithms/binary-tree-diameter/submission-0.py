# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(curr):
            nonlocal diameter
            
            if not curr:
                return 0
            
            left_height =  dfs(curr.left)
            right_height = dfs(curr.right)

            total_height = left_height + right_height
            diameter = max(diameter, total_height)
            return max(left_height, right_height) + 1 # to account for curr
        
        dfs(root)
        
        return diameter
        
