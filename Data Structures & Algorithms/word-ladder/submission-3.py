from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = deque([(beginWord, 1)])
        hash_map = defaultdict(list)
        
        n = len(beginWord)
        
        for i in range(n):
            key = beginWord[:i] + '.' + beginWord[i+1:]
            hash_map[key] += [beginWord]
            
        
        for word in wordList:
            for i in range(n):
                key = word[:i] + '.' + word[i+1:]
                hash_map[key] += [word]
        
        visited_wrds = set(beginWord)
        visited_patterns = set()
        while que:
            wrd, t = que.popleft()
            
            if wrd == endWord:
                return t
            
            neighbors = []
            for i in range(n):
                key = wrd[:i] + '.' + wrd[i+1:]
                if key not in visited_patterns:
                    neighbors += hash_map[key]
                    visited_patterns.add(key)
            
            for neighbor in neighbors:
                if neighbor not in visited_wrds:
                    que.append((neighbor, t+1))
                    visited_wrds.add(neighbor)
        return 0
                
            
            
    
                
