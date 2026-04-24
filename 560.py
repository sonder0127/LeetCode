class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        cnt[0] = 1    #空前缀和的统计
        pre_sum = 0
        ans = 0
        for x in nums:
            pre_sum+=x
            ans+=cnt[pre_sum-k]
            cnt[pre_sum]+=1
        return ans
        # n = len(nums)
        # pre_sum = [0]*(n+1)
        # for i, x in enumerate(nums):
        #     pre_sum[i+1] = pre_sum[i]+x
        
        # cnt = defaultdict(int)
        # ans = 0
        # for sj in pre_sum:
        #     ans += cnt[sj-k]
        #     cnt[sj]+=1
        # return ans
