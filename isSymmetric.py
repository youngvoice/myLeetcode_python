# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and root2:
                if root1.val == root2.val:
                    #if symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)
                    if symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left):
                        return True
                    
                else:
                    return False
            else:
                return False
        
        return symmetric(root, root)
'''
from  collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque()
        queue.append(root)
        queue.append(root)
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if not t1 and not t2:
                continue
            elif t1 and t2:
                if t1.val == t2.val:
                    queue.append(t1.left)
                    queue.append(t2.right)
                    queue.append(t1.right)
                    queue.append(t2.left)
                    continue
                else:
                    return False
            else:
                return False
        return True


