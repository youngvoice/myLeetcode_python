'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        heap = [(nums[i+1] - nums[i], i, i + 1)
                for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in range(k):
            d, root, nei = heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush((nums[nei + 1] - nums[root], root, nei + 1))
        return d

'''


class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo