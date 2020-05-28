# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.cur = 0

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self.nodes_sorted[self.cur]
        #self.cur = self.cur + 1
        self.cur += 1
        return val



    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.cur < len(self.nodes_sorted)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


'''
使用栈递归，可以按递归过程逐个输出
'''