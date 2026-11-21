class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        def dfs(prev, curr):
            neighbors = adj_list[curr]
            for nei in neighbors:
                if nei == prev or nei in visited: # Makes sure we go in one direction
                    continue
                visited.add(nei)
                dfs(curr, nei)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(None, i)
        return count