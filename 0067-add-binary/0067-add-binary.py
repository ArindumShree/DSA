class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        ans=""
        while i>=0 or j>=0 or carry:
            bit_a=0 if i<0 else int(a[i])
            bit_b=0 if j<0 else int(b[j])
            num=bit_a+bit_b+carry
            ans+=str(num%2)
            carry=num//2
            i-=1
            j-=1
        ans=ans[::-1]
        return ans