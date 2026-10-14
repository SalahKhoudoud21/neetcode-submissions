class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.IsEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] == None:
                node.children[index] = TrieNode()
            
            node = node.children[index]
        
        node.IsEndOfWord = True

    def search(self, word: str) -> bool:
        root = self.root
        
        def dfs(index, node):
            if index == len(word) and node.IsEndOfWord:
                return True
            
            if index == len(word):
                return False
            
            char = word[index]
            
            if char == '.':
                for child in node.children:
                    if child != None:
                        if dfs(index + 1, child):
                            return True
                return False

            else:
                ind = ord(char) - ord('a')
                
                if node.children[ind] == None:
                    return False
                
                return dfs(index + 1, node.children[ind])
        
        return dfs(0, root)

                  
                    
                    
        
