'''

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        for i, word_first in enumerate(words):
            for j, word_second in enumerate(words):
                if i != j:
                    combined_word = word_first+word_second
                    # judge
                    if combined_word == combined_word[::-1]:
                        res.append([i, j])
                else:
                    continue
        return res
'''



'''
class Solution:
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def all_valid_suffixes(word):
            valid_suffixes = []
            valid_suffixes.append(word)
            for i in range(len(word)):
                #if word[:i+1] == word[:i+1][::-1]:
                #    valid_suffixes.append(word[i+1:])
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i+1:])
            return valid_suffixes
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes
        word_lookup = {word: i for i, word in enumerate(words)}
        res = []

        for index, word in enumerate(words):
            valid_suffixes = all_valid_suffixes(word) #case 2   ???? 121****
            for suffix in valid_suffixes:
                if suffix[::-1] in word_lookup:
                    if word_lookup[suffix[::-1]] != index:
                        res.append([word_lookup[suffix[::-1]], index])

            valid_prefixes = all_valid_prefixes(word)
            for prefix in valid_prefixes:
                if prefix[::-1] in word_lookup:
                    if word_lookup[prefix[::-1]] != index:
                        res.append([index, word_lookup[prefix[::-1]]])
        return res

'''


'''
class Solution:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
    def insert(self, word: str, index) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
                #cur["isWord"] = False # overlap
            cur = cur[letter]
        cur["index"] = index   

    def search(self, word: str) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                return None
            cur = cur[letter]
        if "index" not in cur:
            return None
        return cur["index"] 
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def all_valid_suffixes(word):
            valid_suffixes = []
            valid_suffixes.append(word)
            for i in range(len(word)):
                #if word[:i+1] == word[:i+1][::-1]:
                #    valid_suffixes.append(word[i+1:])
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i+1:])
            return valid_suffixes
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes
        for i, word in enumerate(words):
            self.insert(word, i)
        
        res = []

        for index, word in enumerate(words):
            valid_suffixes = all_valid_suffixes(word) #case 2   ???? 121****
            for suffix in valid_suffixes:
                i = self.search(suffix[::-1])
                if i != None:
                    if i != index:
                        res.append([i, index])
            

            valid_prefixes = all_valid_prefixes(word)
            for prefix in valid_prefixes:

                i = self.search(prefix[::-1])
                if i != None:
                    if i != index:
                        res.append([index, i])
        return res

'''


'''
利用Trie树优化搜索效率，降低时间复杂度。
对于每一个单词，从后往前遍历字符串，查找在Trie树中是否有对应的单词，找到的单词拼接到当前单词判断是否为回文串。
'''

# wrong version

'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def isPalindrome(word):
            return word == word[::-1]
        ans = []
        wordIndex = {word: index for index,word in enumerate(words)}

        for word in words:
            wordLen = len(word)
            for i in range(wordLen+1):
                # word[:i]
                #judge palindrome
                if isPalindrome(word[:i]):
                    if word[i:][::-1] in wordIndex:
                        if word[i:][::-1] != word:
                            ans.append([wordIndex[word[i:][::-1]], wordIndex[word]])

                if isPalindrome(word[wordLen-i:]):
                    if word[:wordLen-i][::-1] in wordIndex:
                        if word != word[:wordLen-i][::-1]:
                            ans.append([wordIndex[word], wordIndex[word[:wordLen-i][::-1]]])
        res = []
        for elem in ans:
            if elem not in res:
                res.append(elem)
        return res
'''

class Solution:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
    def insert(self, word: str, index) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
                #cur["isWord"] = False # overlap
            cur = cur[letter]
        cur["index"] = index   

    def search(self, word: str) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                return None
            cur = cur[letter]
        if "index" not in cur:
            return None
        return cur["index"]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = set()
        for index, word in enumerate(words):
            self.insert(word, index)
        for index, word in enumerate(words):
            wordLen = len(word)
            for i in range(wordLen+1):
                sucIndex = self.search(word[:i][::-1])
                if sucIndex != None:
                    combineWord = word + words[sucIndex]
                    if combineWord == combineWord[::-1]:
                        if (index, sucIndex) not in ans and index != sucIndex:
                            ans.add((index,sucIndex))
                preIndex = self.search(word[wordLen-i:][::-1])
                if preIndex != None:
                    combineWord = words[preIndex] + word
                    if combineWord == combineWord[::-1]:
                        if (preIndex, index) not in ans and index != preIndex:
                            ans.add((preIndex, index))
        res = [[index1, index2] for index1, index2 in ans]
        return res
        
        



