'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [n1 for n1 in s1 if n1 in s2]
'''
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        if (len(s1) > len(s2)):
            return [n2 for n2 in s2 if n2 in s1]
        else:
            return [n1 for n1 in s1 if n1 in s2]
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return s1 & s2

