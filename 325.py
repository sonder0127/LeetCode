# 力扣 325 题：和等于 k 的最长子数组长度（Maximum Size Subarray Sum Equals k）
# 一、题目描述
# 给定一个整数数组 nums 和一个目标值 k，找到和为 k 的最长连续子数组的长度。如果不存在这样的子数组，返回 0。
# 注意：数组中可包含负数、0、正数。
# 示例 1
# 输入：nums = [1, -1, 5, -2, 3], k = 3
# 输出：4
# 解释：子数组 [1, -1, 5, -2] 和为 3，长度最长。
# 示例 2
# 输入：nums = [-2, -1, 2, 1], k = 1
# 输出：2
# 解释：子数组 [-1, 2] 和为 1。
from collections import defaultdict
def maxSubArrayLen(nums, k):
    pre_sum = {}
    #前缀和的前面得加一个0的前缀和
    pre_sum[0] = -1
    max_len = 0
    cur_sum = 0
    for i, num in enumerate(nums):
        cur_sum+=num
        if cur_sum-k in pre_sum:
            max_len = max(max_len, i-pre_sum[cur_sum-k])
        if cur_sum not in pre_sum:
            pre_sum[cur_sum] = i
    print(max_len)

maxSubArrayLen(nums = [1, -1, 5, -2, 3], k = 3)

#1, 0, 5, 3, 6









def maxSubArrayLen(nums, k):
    pre_sum = {}
    max_len = 0
    cur_sum = 0
    for i, num in enumerate(nums):
        cur_sum+=num
        if cur_sum-k in pre_sum:
            max_len = max(max_len, i - pre_sum[cur_sum-k])
        if cur_sum not in pre_sum:
            pre_sum[cur_sum] = i
    return max_len














def maxSubArrayLen(nums, k):
    # key: 前缀和, value: 第一次出现的索引
    prefix_map = {0: -1}
    current_sum = 0
    max_len = 0

    for i, num in enumerate(nums):
        current_sum += num  # 计算当前前缀和

        # 查找是否存在 prefix[j] = current_sum - k
        if (current_sum - k) in prefix_map:
            # 计算长度 i - j
            max_len = max(max_len, i - prefix_map[current_sum - k])

        # 只存第一次出现的前缀和
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_len