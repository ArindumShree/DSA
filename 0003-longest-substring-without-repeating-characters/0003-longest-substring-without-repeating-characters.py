class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        a=set()
        a.add(s[0])
        ans=1
        i,j=0,1
        while j<n:
            while s[j] in a:
                a.discard(s[i])
                i+=1
            a.add(s[j])
            j+=1
            ans=max(ans,j-i)
        return ans