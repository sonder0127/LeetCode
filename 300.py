class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = 以第i个数结尾的最长递增子序列长度
        dp = [0] * len(nums)  

        # 遍历每个数字 x，位置 i
        for i, x in enumerate(nums):
            
            # 遍历 i 前面所有数字 y，位置 j
            for j, y in enumerate(nums[:i]):
                
                # 如果当前数字 x > 前面的数字 y
                if x > y:
                    # 说明可以接在 y 后面，更新 dp[i]
                    dp[i] = max(dp[i], dp[j])
            
            # 最后 +1：加上自己
            dp[i] += 1

        # 整个 dp 数组里最大的值，就是全局最长递增子序列
        return max(dp)