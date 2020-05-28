'''
# the wrong method (update)
from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def bfs(matrix, i, j):
            neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            visited = set((i, j))
            queue = deque([(i, j)])
            step = -1

            while queue:
                step = step + 1
                layer_nodes = len(queue)
                for node in range(layer_nodes):
                    cur = queue.popleft()
                    if matrix[cur[0]][cur[1]] == 0:
                        return step
                    for neighbor in neighbors:
                        new_i = i + neighbor[0]
                        new_j = j + neighbor[1]
                        if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and (new_i, new_j) not in visited:
                            visited.add((new_i, new_j))
                            queue.append((new_i, new_j))
        #dis = [[0 for j in range(matrix[0])] for i in range(len(matrix))]
        dis = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dis[i][j] = bfs(matrix, i, j)
        return dis

'''


from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def bfs(matrix, i, j):
            neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            visited = set((i, j))
            queue = deque([(i, j)])
            step = -1

            while queue:
                step = step + 1
                layer_nodes = len(queue)
                for node in range(layer_nodes):
                    cur = queue.popleft()
                    if matrix[cur[0]][cur[1]] == 0:
                        return step
                    for neighbor in neighbors:
                        new_i = cur[0] + neighbor[0]
                        new_j = cur[1] + neighbor[1]
                        if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and (new_i, new_j) not in visited:
                            visited.add((new_i, new_j))
                            queue.append((new_i, new_j))
        #dis = [[0 for j in range(matrix[0])] for i in range(len(matrix))]
        dis = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dis[i][j] = bfs(matrix, i, j)
        return dis