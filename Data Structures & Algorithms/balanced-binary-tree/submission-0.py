# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(curr):
            nonlocal balanced

            if not curr:
                return 0 # base case
            

            right_height = dfs(curr.right)
            left_height = dfs(curr.left)

            if right_height > left_height + 1 or left_height > right_height + 1:
                balanced = False
                return 0 # stop here
            
            return max(right_height, left_height) + 1
        
        dfs(root)
        
        return balanced


