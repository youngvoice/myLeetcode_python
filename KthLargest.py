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
                node.cnt += 1 
            else:
                node.right = self.recursive(node.right, val)
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
        '''
        def kthlg(node, k):
            if node.right:
                if k > node.right.cnt:
                    k -= node.right.cnt - 1
                    if k == 0:
                        return node.val
                    else:
                        return kthlg(node.left, k)

                elif k == node.right.cnt:
                    #self.k == node.right.cnt:
                    return node.right.val
                else:
                    return kthlg(node.right, k)
            else:
                k -= 1
                if k == 0:
                    return node.val
                else:
                    #if node.left:#??????????????????????????
                    return kthlg(node.left, k)

        def kthlg2(node, k):
            if not node:
                return None
            if node.right:
                ge = node.right.cnt + 1
            else:
                ge = 1
            if ge == k:
                return node.val
            elif k > ge:
                return kthlg2(node.left, k - ge)
            else:
                #kthlg2(node.right, k - ge)
                return kthlg2(node.right, k)
        '''
        def kthlg3(node, storage):
            if node.right:
                kthlg3(node.right, storage)
            if len(storage) == self.k:
                return
            storage.append(node.val)
            
            if node.left:
                kthlg3(node.left, storage)


            
        self.bst = self.recursive(self.bst, val)
        kthlg3(self.bst, storage)
        ans = storage.pop()
        storage = []
        return ans



        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
