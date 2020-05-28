# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            pivot = left + (right - left) // 2
            print(left, pivot, right)
            res = guess(pivot)
            print(res, pivot)
            if res == -1:
                #left = pivot + 1
                right = pivot - 1
            elif res ==  1:
                #right = pivot - 1
                left = pivot + 1
            else:
                return pivot
            
            