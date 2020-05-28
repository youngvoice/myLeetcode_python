# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Solution:
    def __init__(self):
        self.ans = 0
    def traversal(self, node, depth):
            if not node:
                if self.ans < depth:
                    self.ans = depth
                return
            self.traversal(node.left, depth + 1)
            self.traversal(node.right, depth + 1)
    def maxDepth(self, root: TreeNode) -> int:       
        self.traversal(root, 0)
        return self.ans
    
'''

# top-down
'''
class Solution:
    def __init__(self):
        self.ans = 0
    
    def maxDepth(self, root: TreeNode) -> int:   
        def traversal(node, depth):
            if not node:
                if self.ans < depth:
                    self.ans = depth
                return
            traversal(node.left, depth + 1)
            traversal(node.right, depth + 1)

        traversal(root, 0)
        return self.ans
'''

# bottom-up
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def traversal(node):
            if not node:
                return 0
            left_d = traversal(node.left)
            right_d = traversal(node.right)
            return max(left_d, right_d) + 1
        return traversal(root)
'''
class Solution:
    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth

