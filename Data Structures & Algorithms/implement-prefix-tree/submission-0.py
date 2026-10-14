class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        end = len(word) - 1
        node = self.root
        for i, char in enumerate(word):
            idx = ord(char) - ord('a')
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            
            node = node.children[idx]
            
            if i == end:
                node.isEndofWord = True
            
            

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] != None:
                node = node.children[index]
                continue
            return False
        
        if node.isEndofWord == False:
            return False
        
        return True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if node.children[index] != None:
                node = node.children[index]
                continue
            return False
        
        return True
        
        