from typing import List
class Solution:
    def findMin(self, nums: List[int]):
        left, right = -1, len(nums)-1
        while left+1<right:
            mid = (left+right)//2
            if nums[mid]<nums[-1]:
                right = mid
            else:
                left = mid
        return right
    def lower_bond(self, nums: List[int], target: int, left: int, right: int):
        while left+1<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid
            else:
                right = mid
        return right if nums[right]==target else -1

    def search(self, nums: List[int], target: int) -> int:
        i = self.findMin(nums)
        print(i)
        if target>nums[-1]: #在第一段
            return self.lower_bond(nums, target, -1, i-1)
        else:
            return self.lower_bond(nums, target, i-1, len(nums)-1)


fun=Solution()

print(fun.search(nums=[4,5,6,7,0,1,2], target=0))