"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
class Solution:
    def __init__(self):
        self.res = []
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return self.res
        self.res.append(root.val)
        for child in root.children:
            self.preorder(child)
        return self.res
'''

class Solution:
    def preorder(self, root):
        stack, output = [root, ], []
        if not root:
            return output
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        
        return output