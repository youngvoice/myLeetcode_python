# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            res.append(top.val)
            cur = top.right
        return res

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            cur = top.right
        return res

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            top = stack.pop()
            cur = top.left
        return res[::-1]
'''


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res = [root, ], []
        while stack:
            root = stack.pop()
            if root.left:
                stack.append(root.left)
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            
        return res