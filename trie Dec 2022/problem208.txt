class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children.keys():
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isword = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children.keys():
                return False
            node = node.children[i]
        if node.isword:
            return True
        else:
            return False
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.children.keys():
                return False
            node = node.children[i]
        return True
