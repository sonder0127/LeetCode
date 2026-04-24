class Solution:
    def findMin(self, nums: List[int]) ->int:
        left, right = -1, len(nums)-1
        while left+1<right:
            mid = (left+right)//2
            if nums[mid]<nums[-1]:
                right = mid
            else:
                left = mid
        return right
    def lower_bond(self, nums: List[int], left: int, right: int, target: int) ->int:
        #寻找target出现的第一个位置，最左边第一个
        while left+1<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid
            else:
                right = mid
        return right if nums[right]==target else -1
    def search(self, nums: List[int], target: int) -> int:
        i = self.findMin(nums)
        if target<=nums[-1]:
            return self.lower_bond(nums, i-1, len(nums)-1, target)
        else:
            return self.lower_bond(nums, -1, i-1, target)