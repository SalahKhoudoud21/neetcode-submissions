class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(n)}
        for edge in edges:
            n1, n2 = edge

            # Undirected graph so (0,1) equivalent to (1,0)
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        # A valid tree doesn't have cycles
        visited = set()
        def dfs(prev, node):
            if node in visited: # found a cycle 
                return False
            
            visited.add(node)
            for nei in adj_list[node]:
                if nei == prev: # trying to go in one direction (top to bottom or left to right)
                    continue
                
                if not dfs(node, nei): return False
            
            return True
        
        if not dfs(None, 0): return False
        
        for i in range(n):
            if i not in visited:
                return False
        
        return True
        




