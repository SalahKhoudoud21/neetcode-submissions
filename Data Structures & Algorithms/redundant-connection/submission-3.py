class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.size = [1] * (n+1)
    def find(self, x):
        if self.parents[x] != x: # didnt find the root
            return self.find(self.parents[x])
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False # -> a cycle was found already connected in some way
        
        if  self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parents[root_y] = root_x
        self.size[root_x] += self.size[root_y]

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        for x, y in edges:
            if not union_find.union(x, y):
                return [x, y]
        



       