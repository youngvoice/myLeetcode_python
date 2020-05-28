# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def recursive(node):
'''
            #if not node:    # when the first recursive
            #    node = TreeNode(val)
            #    return node
'''
            if val < node.val:
                if node.left:
                    recursive(node.left)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    recursive(node.right)
                else:
                    node.right = TreeNode(val)
        if not root:
            root = TreeNode(val)
        else:
            recursive(root)
        return root
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#        if not root:
#            root = TreeNode(val)
#        else:
#            if val < root.val:
#                root.left = recursive(root.left, val)
#            else:
#                root.right = recursive(root.right, val)
#        return root
        def recursive(node, val):
            if not node:
                node = TreeNode(val)
            else:
                if val < node.val:
                    node.left = recursive(node.left, val)
                else:
                    node.right = recursive(node.right, val)
            return node
        return recursive(root, val)
'''

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode(val)
            return root
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
        
