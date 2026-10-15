from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        n = len(candidates)
        def backtracking(start, sumSoFar, lista):
            if sumSoFar == target:
                result.append(lista.copy())
                return 0
            
            if sumSoFar > target:
                return 0
            
            for i in range(start, n):
                if i > start: # we started looking at backtracks
                    if candidates[i-1] == candidates[i]:
                        continue
                
                sumSoFar += candidates[i]
                lista += [candidates[i]]
                backtracking(i+1, sumSoFar, lista)
                sumSoFar -= lista.pop()
            
            return 0
        
        backtracking(0, 0, [])
        
        return result
