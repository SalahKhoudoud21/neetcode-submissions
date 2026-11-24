class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.sizes = [1] * (n+1)
    
    def find(self, x):
        if self.parents[x] != x:
            return self.find(self.parents[x])
        return x
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False
        
        if self.sizes[parent_x] < self.sizes[parent_y]:
            parent_x, parent_y = parent_y, parent_x
        
        self.parents[parent_y] = parent_x
        self.sizes[parent_x] += self.sizes[parent_y]
        return True
            

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        unionFind = UnionFind(n)
        for x, y in edges:
            if not unionFind.union(x, y):
                return False # Found a loop (not valid Tree)
        
        return len(edges) == (n - 1) # To see if all nodes interconnected





