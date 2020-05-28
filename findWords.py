

class Solution:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.res = set()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
                #cur["isWord"] = False
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
        if cur["isWord"] != True:
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
    



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        for word in words:
            self.insert(word)
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.__search_word1(board, i, j, marked, self.root, [], m, n)
        return list(self.res)


    def __search_word1(self, board, start_x, start_y, marked, cur_node, word, m, n):
        letter = board[start_x][start_y]
        if letter not in cur_node:
            return False
        next_node = cur_node[letter]
        word.append(letter)
        marked[start_x][start_y] = True
        if "isWord" in next_node:
            if "".join(word) not in self.res:
                self.res.add("".join(word))
        deeper = False
        for direction in self.directions:
            new_x = start_x + direction[0]
            new_y = start_y + direction[1]
            if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y]:
                deeper = deeper or self.__search_word1(board, new_x, new_y, marked, next_node, word, m, n)
            
        if not deeper:
            word.pop()
            marked[start_x][start_y] = False
            return False
        else:
            return True
        

                


        


    def __search_word(self, board, word, index, start_x, start_y, marked, m, n):
        
        #if index == len(word):
        #    return True
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]
        if board[start_x][start_y] == word[index]:
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and self.__search_word(board, word, index + 1, new_x, new_y, marked, m, n):
                    return True
                else:
                    continue
            marked[start_x][start_y] = False
        else:
            return False
