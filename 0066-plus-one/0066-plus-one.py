class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num=''.join(str(d) for d in digits)
        num=int(num)+1
        ans=[int(d) for d in str(num)]
        return ans