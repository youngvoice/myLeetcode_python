class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.cnt = 1

class KthLargest:

    def recursive(self, node, val):
            if not node:
                node = TreeNode(val)
                return node
            if val < node.val:
                node.left = self.recursive(node.left, val)
                #node.cnt += 1 
            else:
                node.right = self.recursive(node.right, val)
                #node.cnt += 1
            node.cnt += 1
            return node
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.bst = None
        
        while nums:
            val = nums.pop()
            self.bst = self.recursive(self.bst, val)


    def add(self, val: int) -> int:
        storage = []
        
        
        def kthlg2(node, k):
            if not node:
                return None
            cur_count = node.cnt
            if node.left:
                left_count = node.left.cnt 
            else:
                left_count = 0
            if node.right:
                right_count = node.right.cnt
            else:
                right_count = 0
            cur_count = cur_count - left_count - right_count
           
            if k <= right_count:
                return kthlg2(node.right, k)
            elif k > (right_count + cur_count):
                return kthlg2(node.left, k - right_count - cur_count)
            else:
                return node.val
        self.bst = self.recursive(self.bst, val)
        return kthlg2(self.bst, self.k)



        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
