class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        idx = 0
        order = ord(word[idx]) - ord('a')
        node = self.root
        # if node.children[order] is None:
        #     node.children[order] = Node()
        #     idx = 1

        while idx < len(word):
            order = ord(word[idx]) - ord('a')
            if node.children[order] is None:
                node.children[order] = Node()

            node = node.children[order]
            if idx == len(word) - 1: node.isEndOfWord = True
            idx += 1
        

    def search(self, word: str) -> bool:
        idx = 0
        order = ord(word[idx]) - ord('a')
        node = self.root

        while idx < len(word):
            order = ord(word[idx]) - ord('a')
            if node.children[order] is None: return False

            node = node.children[order]
            idx += 1

        return node.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        idx = 0
        order = ord(prefix[idx]) - ord('a')
        node = self.root

        while idx < len(prefix):
            order = ord(prefix[idx]) - ord('a')
            if node.children[order] is None: return False

            node = node.children[order]
            idx += 1

        return True
        
        