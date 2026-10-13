class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n=len(nums)
        h_map={}
        for i in range(n):
            if nums[i] in h_map:
                sum_=i-h_map[nums[i]]
                if sum_<=k:
                    return True
                else:
                    h_map[nums[i]]=i
            else:
                h_map[nums[i]]=i
        return False