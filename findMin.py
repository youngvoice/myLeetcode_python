'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right] or len(nums) == 1:
            return nums[left]
        while left <= right:
            print(left, right)
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return nums[pivot + 1]
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot
'''
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        if nums[left] < nums[right - 1] or right == 1:
            return nums[left]
        else:
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= nums[0]:
                    left = mid + 1
                else:
                    right = mid
            if left != len(nums):
                return nums[left]
'''
#  154. Find Minimum in Rotated Sorted Array II
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        if nums[left] < nums[right - 1] or right == 1:
            return nums[left]
        else:
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == nums[0]:
                    if mid == 0:
                        left = mid + 1
                    else:
                        right = right - 1
                        
                elif nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid
            if left != len(nums):
                return nums[left]
            if nums[0] == nums[len(nums) - 1]:
                return nums[0]
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right = right - 1
        return nums[left]
        