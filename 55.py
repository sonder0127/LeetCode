class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_right_arrive = 0
        for i in range(len(nums)):
            if max_right_arrive<i:
                return False
            else:
                max_right_arrive = max(max_right_arrive, i+nums[i])
        return True