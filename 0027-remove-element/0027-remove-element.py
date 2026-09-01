class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        # b=n
        # for i in range(b-1,-1,-1):
        #     if nums[i]==val:
        #         nums.pop(i)
        k=0
        for i in range(n):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k