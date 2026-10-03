class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l,r=0,0
        max_freq=0
        ans=0
        hmap={}
        while r<n:
            hmap[s[r]]=hmap.get(s[r],0)+1
            max_freq=max(max_freq,hmap[s[r]])
            while r-l-max_freq+1>k:
                hmap[s[l]]-=1
                l+=1
            ans = max(ans, r - l + 1)
            r+=1
        return ans