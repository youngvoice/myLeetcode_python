# 学习迭代器写法
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, mask, index, maxIndex, numRows, numCols):
            #print("dfs", i, j, numRows, numCols)
        
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            index += 1
            if index < maxIndex: # the word has left
                letter = word[index]
                #print(letter)
                #for neighbor
                res = False
                for direction in directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    #if new_i == 0 and new_j == 1:
                        #print("mask[0][1]", mask[new_i][new_j])
                    #if (new_i >= 0 and new_i < numRows) and (new_j >= 0 and new_j < numCols) and (not mask[new_i][new_j]):
                    #print("wrong", new_j, numCols)
                    if (new_i >= 0 and new_i < numRows) and (new_j >= 0 and new_j < numCols) and (not mask[new_i][new_j]):
                        #print("new", new_i, new_j)

                        if not board[new_i][new_j] == letter:
                            continue
                        else:
                            new_mask = [[col for col in row] for row in mask]
                            new_mask[new_i][new_j] = 1
                            #print("position", new_i, new_j)
                            res = res or dfs(new_i, new_j, new_mask, index, maxIndex, numRows, numCols)
                    else:
                        continue
                
                return res
            else:
                return True



        numRows = len(board)
        numCols = len(board[0])
        res = False
        for i in range(numRows):
            for j in range(numCols):
                if board[i][j] == word[0]:
                    mask = [[0 for m in range(numCols)] for n in range(numRows)]
                    mask[i][j] = 1
                    index = 0
                    maxIndex = len(word)
                    res = res or dfs(i, j, mask, index, maxIndex, numRows, numCols)
                else:
                    continue
        return res
'''

class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.__search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

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

