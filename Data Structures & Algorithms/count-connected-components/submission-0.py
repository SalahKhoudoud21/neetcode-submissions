class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        for edge in edges:
            n1,n2 = edge
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        visited = set()
        def dfs(prev, node):
            visited.add(node)
            for nei in adj_list[node]:
                if nei == prev or nei in visited:
                    continue
                
                dfs(node, nei)
            return
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(None, i)
        return count