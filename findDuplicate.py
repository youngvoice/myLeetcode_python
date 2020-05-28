'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
'''
'''
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
'''


'''
how to be a cycle
'''
class Solution:
    def findDuplicate(self, nums):
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
            # Find the 'entrance' to the cycle.
            ptr1 = nums[0]
            ptr2 = tortoise
            while ptr1 != ptr2:
                ptr1 = nums[ptr1]
                ptr2 = nums[ptr2]
            return ptr1

