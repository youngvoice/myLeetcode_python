# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def calHeight(node):
            if not node:
                return -1
            height = 1 + max(calHeight(node.left), calHeight(node.right))
            return height
        
        if not root:
            return True
        left_height = calHeight(root.left)
        right_height = calHeight(root.right)
        if abs(left_height - right_height) <= 1:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
        else:
            return False
