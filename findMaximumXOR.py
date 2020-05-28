class Solution:
    def __init__(self):
        self.trie = {}
    def insert(self, decimalNum):
        cur = self.trie
        for i in range(31, -1, -1):
            bit = (decimalNum >> i) & 1
        #for bit in binString:
            if bit not in cur:
                cur[bit] = {}
            cur = cur[bit]
        cur["#"] = {}
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            self.insert(num)
        for num in nums:
            cur = self.trie
            numRes = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit == 1:
                    if 0 in cur:
                        numRes += (1 << i)#2^i
                        cur = cur[0]
                    else:
                        cur = cur[1]
                        
                else:
                    if 1 in cur:
                        numRes += (1 << i)
                        cur = cur[1]
                    else:
                        cur = cur[0]
            
            res = max(res, numRes)
        return res
                
                    


