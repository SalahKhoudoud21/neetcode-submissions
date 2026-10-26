class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        out = []
        rows, cols = len(board), len(board[0])
        visited = set()

        # Building our Trie from the words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                index = ord(char) - ord('a')
                if not node.children[index]:
                    node.children[index] = TrieNode()
                node = node.children[index]
            node.is_end_of_word = True

        def backtracking(r, c, node, w):
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or ((r,c) in visited):
                return
            
            item = board[r][c]
            index = ord(item) - ord('a')
            
            if not node.children[index]:
                return
            
            node = node.children[index]
            w += item
            visited.add((r,c))

            if node.is_end_of_word:
                out.append(w)
                node.is_end_of_word = False
            
            backtracking(r+1, c, node, w)
            backtracking(r-1, c, node, w)
            backtracking(r, c+1, node, w)
            backtracking(r, c-1, node, w)
            
            w = w[:-1]
            visited.remove((r,c))

            return
        
        for r in range(rows):
            for c in range(cols):
                backtracking(r, c, root, '')
        
        return out

    

    
    
    
