class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i, h in enumerate(height):
            while stack and h>=height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                dh = min(h, height[stack[-1]]) - height[top]
                ans += width*dh
            stack.append(i)
        return ans