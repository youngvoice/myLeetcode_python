# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def preOrderTraversal(node, accumulate, sum):
            if not node:
                if accumulate == sum:
                    return True
                else:
                    return False
            else:
                accumulate = accumulate + node.val
                if preOrderTraversal(node.left, accumulate, sum) or preOrderTraversal(node.right, accumulate, sum):
                    return True
                else:
                    return False
                
        accumulate = 0
        if not root:
            return False
        return preOrderTraversal(root, accumulate, sum)
'''


'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def preOrderTraversal(node, accumulate, sum):
            if node:
                accumulate = accumulate + node.val

                if not node.left and not node.right:
                    if accumulate == sum:
                        return True
                    else:
                        return False
                else:
                    left_res = False
                    right_res = False
                    if node.left:
                        left_res = preOrderTraversal(node.left, accumulate, sum)
                    if node.right:
                        right_res = preOrderTraversal(node.right, accumulate, sum)
                    if left_res or right_res:
                        return True
                    else:
                        return False
                
        accumulate = 0
        if not root:
            return False
        return preOrderTraversal(root, accumulate, sum)

'''

'''
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
'''
# wrong

class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = [(root, sum - root.val)]
        curr = root
        sum = sum - curr.val
        while curr or stack:
            while curr:

                if not curr.left and not curr.right:
                    if sum == 0:
                        return True
                stack.append((curr, sum - curr.val))
                curr = curr.left
            curr, sum = stack.pop()
            curr = curr.right
        
        return False


# 关联式存储
'''
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
'''
