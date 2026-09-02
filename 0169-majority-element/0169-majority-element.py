class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        major=nums[0]
        for i in dict:
            if dict[i]>dict[major]:
                major=i
        return major