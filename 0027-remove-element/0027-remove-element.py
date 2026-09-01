class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        b=n
        for i in range(b-1,-1,-1):
            if nums[i]==val:
                nums.pop(i)
