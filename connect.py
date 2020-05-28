"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            preIndividual = queue.popleft()
            print(preIndividual.val)
            if preIndividual.left:
                queue.append(preIndividual.left)
            if preIndividual.right:
                queue.append(preIndividual.right)
            if level_size > 1:
                for i in range(level_size - 1):
                    individual = queue.popleft()
                    print(individual.val)
                    preIndividual.next = individual
                    if individual.left:
                        queue.append(individual.left)
                    if individual.right:
                        queue.append(individual.right)
                    preIndividual = individual
                individual.next = None
            else:
                preIndividual.next = None
        return root
