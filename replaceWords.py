'''
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        ans = ""
        while True:
            word = getWord(sentence)
            if word:
                root = findRoot(word)
                ans = ans + root + " "
            else:
                break

'''
'''
def replaceWords(self, dict, sentence):
    rootset = set(dict)
    def replace(word):
        for i in range(1, len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word
    return " ".join(map(replace, sentence.split()))

'''
import collections


class Solution:

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
    def replaceWords(self, roots, sentence):
        for root in roots:
            self.insert(root)
        def replace(word):
            cur = self.root
            prefix = ""
            for letter in word:

                if letter not in cur:
                        return word
                else:
                    prefix += letter
                    cur = cur[letter]
                    if "isWord" in cur and cur["isWord"]:
                        return prefix
            return word
        return " ".join(map(replace, sentence.split()))
        
        

