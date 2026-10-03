class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap={}
        n=len(nums)
        for i in range(n):
            req=target-nums[i]
            if req in hmap:
                return[i,hmap[req]]
            else:
                hmap[nums[i]]=i
        

        