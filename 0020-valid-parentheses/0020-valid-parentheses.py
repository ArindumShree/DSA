class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2==1:
            return False
        st=[]
        for i in s:
            if i=='[' or i=='{' or i =='(':
                st.append(i)
            else:
                if not st:
                    return False
                top=st.pop()
                if i==')' and top!='(':
                    return False
                elif i==']' and top!='[':
                    return False
                elif i=='}' and top!='{':
                    return False
        if not st:
            return True
        return False
                