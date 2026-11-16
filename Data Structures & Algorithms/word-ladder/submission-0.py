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
        
        visited = set(que)
        while que:
            wrd, t = que.popleft()
            
            if wrd == endWord:
                return t
            
            neighbors = []
            for i in range(n):
                key = wrd[:i] + '.' + wrd[i+1:]
                neighbors += hash_map[key]
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    que.append((neighbor, t+1))
                    visited.add(neighbor)
        return 0
                
            
            
    
                
