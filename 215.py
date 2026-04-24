import random 
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [num for num in nums if num > pivot]
        mid = [num for num in nums if num==pivot]
        right = [mid for num in nums if num < pivot]

        L = len(left)
        M = len(mid)
        R = len(right)

        if k<=L:
            self.findKthLargest(left, k)
        elif k<=L+M:
            return pivot
        else:
            self.findKthLargest(right, k-L-M)
