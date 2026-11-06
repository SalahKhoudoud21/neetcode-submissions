class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        order = []
        visited = set()
        def dfs(course):
            if course in visited: # cycle
                return False
            
            
            prereqs = adj_list[course]
            if not prereqs:
                if course not in order:
                    order.append(course)
                return True
            
            visited.add(course)
            for pre in prereqs:
                if not dfs(pre): return False
            
            # all prereqs completed successfully
            visited.remove(course)
            adj_list[course] = []
            order.append(course)
            return True
        
        for course in range(numCourses):
            if course not in order:
                if not dfs(course): return []
        
        return order
            