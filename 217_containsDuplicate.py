'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        for i in range(1, len(nums)):
            if sorted_list[i] == sorted_list[i - 1]:
                return True
        return False
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elem = set()
        for e in nums:
            if e is not in unique_elem:
                unique_elem.add(e)
            else:
                return True
        return False