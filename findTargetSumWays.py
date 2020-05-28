'''
class Solution:
    count = 0
    def calculate(self, nums:List[int], S: int, i: int, sum: int):
        if i == len(nums):
            if sum == S: 
                self.count = self.count + 1
        else:
            self.calculate(nums, S, i+1, sum + nums[i])
            self.calculate(nums, S, i+1, sum - nums[i])
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.calculate(nums, S, 0, 0)
        return self.count
                
'''

class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dp = {}
        res = self.helper(nums, S, 0, 0, dp)
        return res
    
    def helper(self, nums, S, i, sum, dp):
        #if i < len(nums):
        if i < len(nums) and (i, sum) not in dp:
            cnt1 = self.helper(nums, S, i + 1, sum + nums[i], dp)
            cnt2 = self.helper(nums, S, i + 1, sum - nums[i], dp)
            dp[(i, sum)] = cnt1 + cnt2
        return dp.get((i, sum), S == sum)




        
        