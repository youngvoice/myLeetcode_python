# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def recursive(node):
            if not node:
                return None
            l = recursive(node.left)
            if l:
                return l        
            if node.val == val:
                return node
            r = recursive(node.right)
            if r:
                return r    

        return recursive(root)
'''

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
