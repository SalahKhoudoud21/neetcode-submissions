"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        og_clone = {}
        stack = [node]
        while stack:
            curr = stack.pop()
            
            if curr not in og_clone:
                og_clone[curr] = Node(curr.val)
            
            for neighbor in curr.neighbors:
                if neighbor not in og_clone:
                    og_clone[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                og_clone[curr].neighbors += [og_clone[neighbor]]
                
        return og_clone[node]


