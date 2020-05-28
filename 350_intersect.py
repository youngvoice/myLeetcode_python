'''
fatal error 
some caution to write for loop 
'''
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for e in nums1:
            if e in nums2:
                nums1.remove(e)
                nums2.remove(e)
                
                result.append(e)
                print(e)
                print(nums1)
                print(nums2)
            else:
                continue
        return result
'''
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = [i for i in nums1]
        n2 = [i for i in nums2]

        result = []
        for e in nums1:
            if e in n2:
                n1.remove(e)
                n2.remove(e)
                
                result.append(e)
                
            else:
                continue
        return result
'''
# time optim
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        if len(nums1) > len(nums2):
            m1 = collections.defaultdict(int)
            for n1 in nums1:
                m1[n1] += 1
            for n2 in nums2:
                if n2 in m1 and m1[n2] > 0:
                    m1[n2] -= 1
                    ret.append(n2)
        
        else:
            m2 = collections.defaultdict(int)
            for n2 in nums2:
                m2[n2] += 1
            for n1 in nums1:
                if n1 in m2 and m2[n1] > 0:
                    m2[n1] -= 1
                    ret.append(n1)
        
        return ret
