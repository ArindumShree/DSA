class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        curr_sum=0
        ans=0
        for a in nums:
            curr_sum+=a

            req=curr_sum-k

            if req in hashmap:
                ans+=hashmap[req]
            hashmap[curr_sum]=hashmap.get(curr_sum,0)+1
        return ans