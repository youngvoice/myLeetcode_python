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
        self.ans = []
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return self.ans
        for child in root.children:
            self.postorder(child)
        self.ans.append(root.val)
        return self.ans
'''

#wrong
'''
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack, ans = [], []
        while root.children:
            stack.append(root)
            stack.extend(root.children[::-1])
            root = stack.pop()
        ans.append(root.val)
        root = stack.pop()
'''

class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        stack, output = [root ,], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
        return  output[::-1]
        