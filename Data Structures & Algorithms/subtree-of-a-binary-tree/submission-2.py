# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        stack = [root]
        nodes_of_interest = []
        
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                nodes_of_interest.append(node)
            
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            
        
        def compare_trees(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            return compare_trees(node1.left, node2.left) and compare_trees(node1.right, node2.right)
            
            
        
        if not nodes_of_interest:
            return False
        
        for node in nodes_of_interest:
            subtree_present = compare_trees(node, subRoot)
            if subtree_present:
                return subtree_present
        
        return False

        


        