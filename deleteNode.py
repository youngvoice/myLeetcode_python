#??????????????????????????????????????????????????????????
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def recursive(node):
            if node.left:
                if key == node.left.val:
                    #swap
                    cur = node.left
                    if not cur.left and not cur.right:
                        node.left = None
                    elif cur.left and not cur.right:

                    elif not cur.left and cur.right:

                    else:

            if node.right:
                if key == node.right.val:
                    #swap
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # root.val == key
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
        


