class Solution:
    def calculate(self, s: str) -> int:
        st=[]
        ans=0
        num=0
        sign=+1
        for i in s:
            if i.isnumeric():
                num=num*10+int(i)
            elif i=='-':
                ans+=num*sign
                num=0
                sign=-1
            elif i=='(':
                st.append(ans)
                st.append(sign)
                ans=0
                sign=+1
            elif i=='+':
                ans+=sign*num
                num=0
                sign=+1
            elif i==')':
                ans+=sign*num
                sign=st.pop()
                previous_result=st.pop()
                ans=previous_result+sign*ans
                num=0
                sign=+1
        ans+=sign*num
        return ans