# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        stack = [root]
        preorder_str = []
        while stack: # preorder
            node = stack.pop()
            if not node:
                preorder_str += ["N"]
                continue
            
            preorder_str.append(str(node.val))
            
            stack.append(node.right)
            stack.append(node.left)
        
        return ",".join(preorder_str)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        i = 0
        def dfs(node):
            nonlocal i
            
            if i == len(preorder) - 1:
                return None
            
            if node == "N":
                i += 1
                return None
            
            else:
                node = TreeNode(node)
                i += 1
                
            node.left = dfs(preorder[i])
            node.right = dfs(preorder[i])

            return node
        
        return dfs(preorder[i])
            
            



        