# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# the wrong version
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursive(curNode):
            if not curNode:
                return True
            cleft = False
            cright = False
            if curNode.left:
                if curNode.val > curNode.left.val:
                    cleft = True
                else:
                    cleft = False
            else:
                cleft = True
                
            if curNode.right:
                if curNode.val < curNode.right.val:
                    cright = True
                else:
                    cright = False
            else:
                cright = True
                
            
            if cleft and cright:
                if recursive(curNode.left) and recursive(curNode.right):
                    return True
                else:
                    return False
                
            else:
                return False

        return recursive(root)
'''

class Solution:
    def isValidBST(self, root):
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root)
