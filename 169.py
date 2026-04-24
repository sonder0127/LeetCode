class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = hp = 0
        for x in nums:
            if hp==0:
                ans = x
                hp = 1
            else:
                if x==ans:
                    hp+=1
                else:
                    hp-=1
        return ans
        # nums.sort()
        # return nums[len(nums)//2]

        # counts = collections.Counter(nums)
        # ans = max(counts.keys(), key=counts.get)
        # counts = collections.Counter(nums)
        # print(counts.keys())
        # print(counts.items())
        # max_count = 0
        # target = None
        # for num, cnt in counts.items():
        #     if cnt>max_count:
        #         target = num
        #         max_count = cnt
        # print(target)
