from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)  # 创建一个长度为amount + 1的列表dp，初始值为float('inf')，表示每个金额的最少硬币数初始为无穷大
        dp[0] = 0  # 凑出金额0所需的硬币数为0
        for i in range(1, amount + 1):  # 遍历从1到amount的每一个金额
            for c in coins:  # 对每一个金额，遍历所有的硬币面额
                if i - c < 0:  # 如果当前金额i减去硬币面额c小于0，说明该硬币面额太大，无法用于凑出金额i，跳过本次循环
                    continue
                dp[i] = min(dp[i], dp[i - c] + 1)  # 更新dp[i]为dp[i]和dp[i - c] + 1中的较小值，即取凑出金额i的最少硬币数
        return dp[amount] if dp[amount]!= float('inf') else -1  # 如果dp[amount]不为无穷大，说明能凑出目标金额，返回dp[amount]；否则返回-1