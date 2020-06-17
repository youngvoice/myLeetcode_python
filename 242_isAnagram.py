'''
histogram based on dict
'''
'''
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hist = defaultdict(int)
        for c in s:
            hist[c] += 1
        for c in t:
            hist[c] -= 1
        for k, v in hist.items():
            if v != 0:
                return False
        return True
'''

'''
sort
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len_s):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True

        
