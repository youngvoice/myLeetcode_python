# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(curr, ret):
            if curr:
                ret.append(curr.val)
                traversal(curr.left, ret)
                traversal(curr.right, ret)
            else:
                return
        ret = []
        curr = root
        traversal(curr, ret)
        return ret
'''

class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output

    

