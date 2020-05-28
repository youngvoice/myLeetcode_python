class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            guess_squared = mid * mid
            if num == guess_squared:
                return True
            elif num < guess_squared:
                right = mid - 1
            else:
                left = left + 1
        return False