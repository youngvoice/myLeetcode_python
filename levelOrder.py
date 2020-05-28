# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            queue = deque()
            res = []
            queue.append(root)
            while queue:
                line = []
                size = len(queue)
                for i in range(size):
                    cur = queue.popleft()
                    line.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                #print(line)
                res.append(line)
            return res
'''

# N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.children:
                    queue.extend(node.children)
            ans.append(level)
        return ans
            



        
