class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        a=1
        for i in range(2,n):
            if nums[i]==nums[a]:
                if nums[a-1]==nums[a]:
                    continue
                    
                else:
                    a+=1
                    nums[a]=nums[i]
            else:
                a+=1
                nums[a]=nums[i]
        return a+1