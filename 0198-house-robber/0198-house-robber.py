class Solution:
    def solve(self,n,nums,dp):
        if n==0:
            return nums[0]
        if n==1:
            return max(nums[0],nums[1])
        if dp[n]!=-1:
            return dp[n]
        dp[n] = max(nums[n] + self.solve(n-2,nums,dp),self.solve(n-1,nums,dp))
        return dp[n]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        return self.solve(n-1,nums,dp)