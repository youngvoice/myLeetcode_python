'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot - 1

            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x
        while left <= right:
            pivot = left + (right - left) // 2
            if x < pivot*pivot:
                right = pivot - 1
            elif x >= (pivot + 1)*(pivot + 1):
                left = pivot + 1
            else:
                return pivot
        #return pivot

