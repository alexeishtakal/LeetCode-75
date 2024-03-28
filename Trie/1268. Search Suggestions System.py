class TrieNode:
    def __init__(self, character):
        self.character = character
        self.words = []
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
            node.words.append(word)
        node.end_of_word = True

    def find(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return ''
        return node.words[:3]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in sorted(products):
            trie.insert(product)
        result = []
        for i in range(1, len(searchWord)+1):
            result.append(trie.find(searchWord[:i]))
        return result