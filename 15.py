class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            first_num = nums[i]
            if i>0 and first_num == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left<right:
                s = first_num + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left+=1
                else:
                    ans.append([first_num, nums[left], nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    right-=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
        return ans