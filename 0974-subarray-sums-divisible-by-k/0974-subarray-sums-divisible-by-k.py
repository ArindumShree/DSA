class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        curr_sum=0
        ans=0

        for a in nums:
            curr_sum+=a
            rem=curr_sum%k

            if rem in hashmap:
                ans+=hashmap[rem]
            hashmap[rem]=hashmap.get(rem,0)+1
        return ans