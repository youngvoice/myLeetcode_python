'''
histogram based on dict
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
        