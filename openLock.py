'''
import collections
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1,1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        
        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}

        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

'''
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        queue = deque(["0000"])
        visited = set(["0000"])
        dead = set(deadends)
        step = -1

        while (queue):
            step += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return step
                if cur in dead:
                    continue
                for next in neighbors(cur):#neighbor
                    if next not in visited:
                        queue.append(next)
                        visited.add(next)
                    '''
                    if next not in visited and next not in dead:
                        queue.append(next)
                        visited.add(next)
                    '''
        return -1




