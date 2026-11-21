class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * (n)
    
    def find(self, x):
        if self.parents[x] != x: # Didnt find root node
            return self.find(self.parents[x])
        return x # found the root (The parent)
    
    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)
        
        if par_x == par_y: # found a cycle
            return False
        
        if self.sizes[par_x] < self.sizes[par_y]:
            par_x, par_y = par_y, par_x
        
        self.parents[par_y] = par_x
        self.sizes[par_x] += self.sizes[par_y]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        unionFind = UnionFind(n)
        
        for x, y in edges:
            if not unionFind.union(x,y): # Found a cycle
                return False
        
        return n in set(unionFind.sizes)
