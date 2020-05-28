'''
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur["isWord"] = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def recursiveSearch(word, i, root):
            cur = root
            for letter in word:
                i += 1
                if letter == ".":
                    if len(list(cur)) >= 1:
                        res = False
                        for k, v in cur.items():
                            if k == "isWord":
                                continue
                            res = res or recursiveSearch(word[i+1:], i, v)
                        return res
                    else:
                        return False
                else:
                    if letter not in cur:
                        return False
                    cur = cur[letter]
            if "isWord" not in cur:
                return False
            return True

        i = -1
        cur = self.root
        for letter in word:
            i += 1
            if letter == ".":
                if len(list(cur)) >= 1:
                    res = False
                    for k, v in cur.items():
                        if k == "isWord":
                            continue
                        #cur = v
                        res = res or recursiveSearch(word[i+1:], i, v)
                    return res
                else:
                    return False 
            else:
                if letter not in cur:
                    return False
                cur = cur[letter]
        if "isWord" not in cur:
            return False
        return True



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

'''

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.lookup = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.lookup
        for letter in word:
            tree = tree.setdefault(letter, {})
        tree["#"] = {}


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(word, tree):
            if not word:
                if "#" in tree:
                    return True
                return False
            if word[0] == ".":
                for t in tree:
                    if helper(word[1:], tree[t]):
                        return True
            elif word[0] in tree:
                if helper(word[1:], tree[word[0]]):
                    return True
            return False

        def helper2(word, tree):
            if not word:
                if "#" not in tree:
                    return False
                else:
                    return True
            if word[0] == ".":
                res = False
                for letter in tree:
                    res = res or helper2(word[1:], tree[letter])
                return res
            else:
                if word[0] not in tree:
                    return False
                else:
                    return helper2(word[1:], tree[word[0]])


        return helper2(word, self.lookup)

        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)