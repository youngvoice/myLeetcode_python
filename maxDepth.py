"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    
    def maxDepth(self, root: 'Node') -> int:
        
        def recursive(node):
            if not node:
                return 0
            subtreeDeepth = []
            for child in node.children:
                subtreeDeepth.append(recursive(child))
            if not subtreeDeepth:
                deep = 1 + max(subtreeDeepth)
            else:
                deep = 1
            return deep
        return recursive(root)
        