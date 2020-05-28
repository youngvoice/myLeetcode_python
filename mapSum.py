'''

class TreeNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        self.isKey = False
class MapSum:

    def __init__(self):
        
        self.root = TreeNode()

        

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.isKey = True
        cur.val = val
        

    def sum(self, prefix: str) -> int:

        def longStr(cur):
            nonlocal s
            for _, node in cur.children.items():
                if node.isKey:
                    s += node.val
            
                if node.children:
                    longStr(node)
                

        s = 0
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return s
            cur = cur.children[c]
        
        # cur
        if cur.isKey:
            s += cur.val
        longStr(cur)
        return s
        
        

        




        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


'''

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        trie
        

    def insert(self, key: str, val: int) -> None:
        

    def sum(self, prefix: str) -> int:
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)