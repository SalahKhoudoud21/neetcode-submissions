class Solution:
    def partition(self, s: str) -> List[List[str]]:
        combinations = []
        n = len(s)
        def backtracking(start, combination):
            if start == n:
                combinations.append(combination.copy())
                return

            for i in range(start, n): # trying every possible substring starting at start           
                current = s[start:i+1]

                if current == current[::-1]:
                    combination.append(current)

                    backtracking(i+1, combination)

                    combination.pop()
            
            return
        
        backtracking(0, [])
        return combinations




                

                


                

                

            
            

            
            

