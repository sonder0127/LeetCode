class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 1. 创建 dp 数组，dp[i] = 第 i 个丑数
        dp = [0] * (n + 1)
        
        # 2. 第一个丑数就是 1（规定）
        dp[1] = 1
        
        # 3. 三个指针，初始都指向第 1 个丑数（下标 1）
        # p2：代表下一个丑数可以由 dp[p2] * 2 得到
        # p3：代表下一个丑数可以由 dp[p3] * 3 得到
        # p5：代表下一个丑数可以由 dp[p5] * 5 得到
        p2 = p3 = p5 = 1
        
        # 4. 从第 2 个丑数开始算，一直算到第 n 个
        for i in range(2, n + 1):
            # 计算三个指针当前能生成的丑数
            num2 = dp[p2] * 2
            num3 = dp[p3] * 3
            num5 = dp[p5] * 5
            
            # 5. 下一个丑数 = 三个数里最小的那个（保证从小到大）
            dp[i] = min(num2, num3, num5)
            
            # 6. 哪个指针生成了当前丑数，就把这个指针 +1（向后走）
            # 注意：这里是 三个 if，不是 elif！
            # 因为可能两个指针算出同样的数，要同时移动
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        # 7. 第 n 个丑数就是答案
        return dp[n]