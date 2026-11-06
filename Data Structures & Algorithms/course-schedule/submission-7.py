class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: # edge case
            return True
    
        adj_list = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            adj_list[crs].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited: # Cycle was detected
                return False
            
            prereqs = adj_list[course]
            if not prereqs: # base case
                return True
            
            visited.add(course)
            for pre in prereqs:
                if not dfs(pre):
                    return False
            visited.remove(course)
            adj_list[course] = [] # since we removed it from visited
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        
        return True
                
            


        