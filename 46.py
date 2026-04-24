from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n        # 存放当前正在生成的排列（结果的“草稿”）
        on_path = [False] * n # 标记：第j个数字是否已经被用过（True=用过）
        ans = []              # 存放最终所有排列

        # DFS 递归函数：i 表示现在要填第 i 个位置（从0开始）
        def dfs(i):
            # 1. 递归终止条件：所有位置都填满了（i == n）
            if i == n:
                ans.append(path.copy())  # 把当前排列加入答案
                return

            # 2. 遍历所有数字，尝试选一个没用过的填到第i位
            for j, on in enumerate(on_path):
                if not on:  # 如果第j个数字 没被用过
                    # --- 做选择 ---
                    path[i] = nums[j]    # 把数字 nums[j] 放到第i个位置
                    on_path[j] = True    # 标记：这个数字已经用了

                    # 递归：去填下一个位置 i+1
                    dfs(i + 1)

                    # --- 撤销选择（回溯核心！）---
                    on_path[j] = False   # 取消标记，恢复原状，供下一次循环使用

        # 从第 0 个位置开始填
        dfs(0)
        return ans