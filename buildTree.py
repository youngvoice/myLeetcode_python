'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            nonlocal i
            if in_left > in_right:
                return None
            #print(i)
            root_val = preorder[i]
            i = i + 1
            #root = TreeNode()
            #root.val = root_val
            root = TreeNode(root_val)
            index = idx_map[root_val]
            
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            
            return root
        i = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

