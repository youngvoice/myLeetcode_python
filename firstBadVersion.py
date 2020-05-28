# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n + 1
        while left < right:
            mid = (left + right) // 2
            if (mid != 1 and isBadVersion(mid) and not isBadVersion(mid - 1)) or (mid == 1 and isBadVersion(mid)):
                return mid
            elif not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid

            if left != n + 1 and ((left != 1 and not isBadVersion(left - 1) and isBadVersion(left)) or (left == 1 and isBadVersion(left))):
                return left
