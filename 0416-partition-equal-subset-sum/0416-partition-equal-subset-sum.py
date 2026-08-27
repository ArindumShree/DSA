class Solution:
    def solve(self,idx,add,nums,total,dp):
        if add>total:
            return False
        elif add==total:
            return True
        elif idx>=len(nums):
            return False
        if dp[idx][add] != -1:
            return dp[idx][add]
        not_take=self.solve(idx+1,add,nums,total,dp)
        take=self.solve(idx+1,add+nums[idx],nums,total,dp)
        dp[idx][add] = take or not_take
        return dp[idx][add]
    def canPartition(self, nums: List[int]) -> bool:
        sum_=0
        for i in nums:
            sum_+=i
        if sum_%2!=0:
            return False
        total=sum_//2
        dp = [[-1] * (total + 1) for _ in range(len(nums))]
        return self.solve(0,0,nums,total,dp)