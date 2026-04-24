class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        max_len = 0
        left = 0
        right = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i]==s[j]:
                    if j-i<=1:
                        dp[i][j]=True
                    elif dp[i+1][j-1]:
                        dp[i][j]=True
                    if dp[i][j]:
                        cur_max = j-i+1
                        if cur_max>max_len:
                            max_len = cur_max
                            left = i
                            right = j
        return s[left:right+1]

        


                    

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 记录最长回文的起止位置
        max_start = 0
        max_end = 0
        
        # 遍历每个可能的中心点
        for i in range(len(s)):
            # 情况1：奇数长度回文，中心 i
            l1, r1 = self.expand(s, i, i)
            # 情况2：偶数长度回文，中心 i 和 i+1
            l2, r2 = self.expand(s, i, i + 1)
            
            # 选更长的那个
            if r1 - l1 > max_end - max_start:
                max_start, max_end = l1, r1
            if r2 - l2 > max_end - max_start:
                max_start, max_end = l2, r2
        
        return s[max_start:max_end + 1]

    # 从 l, r 向两边扩散，返回最长回文的左右下标
    def expand(self, s, l, r):
        # 只要左右相等就继续扩散
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # 最后一次不满足，回退一步
        return l + 1, r - 1