# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder and not inorder:
        #     return None
        
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root

        indices = {val: idx for idx, val in enumerate(inorder)}
        pre_index = 0

        def dfs(l, r):
            nonlocal indices, pre_index
            
            if l > r:
                return None
            
            value = preorder[pre_index]
            mid = indices[value]
            pre_index += 1
            root = TreeNode(value)
            root.left = dfs(l,mid-1) # left subtree
            root.right = dfs(mid+1,r) # right subtree
            return root
        
        return dfs(0, len(inorder)-1)
            


        