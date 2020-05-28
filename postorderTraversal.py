'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(curr, ret):
            if curr:
                traversal(curr.left, ret)
                traversal(curr.right, ret)
                ret.append(curr.val)
            else:
                return
        ret = []
        curr = root
        traversal(curr, ret)
        return ret
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ret = []
        curr = root
        while curr or stack:
            while curr:
                ret.append(curr.val)
                stack.append(curr)
                curr = curr.right
            top = stack.pop()
            curr = top.left
        return ret[::-1]



