'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = set()
        for i in nums:
            if i not in single:
                single.add(i)
            else:
                single.remove(i)
        return single.pop()
'''
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_count = collections.defaultdict(int)
        for k in nums:
            dict_count[k] += 1
        for k, v in dict_count.items():
            if v == 1:
                return k
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in nums:
            single = single^i 
        return single 
