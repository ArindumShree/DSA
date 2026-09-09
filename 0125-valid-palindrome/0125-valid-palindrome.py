import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned=re.sub(r'[^A-Za-z0-9]', '', s)
        l,r=0,len(cleaned)-1
        while l<r:
            if cleaned[l]!=cleaned[r]:
                return False
            else:
                l+=1
                r-=1
        return True