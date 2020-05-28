# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def recursive(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = recursive(left, mid - 1)
            node.right = recursive(mid + 1, right)
            return node
        return recursive(0, len(nums) - 1)