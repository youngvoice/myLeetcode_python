'''
class TreeNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.isWord = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if cur.isWord:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
                #cur["isWord"] = False # overlap
            cur = cur[letter]
        cur["isWord"] = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        if "isWord" not in cur:
            return False
        return True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)