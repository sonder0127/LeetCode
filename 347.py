from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        num_count = Counter(nums)
        sorted_nums = sorted(num_count.keys(), key=lambda x: -num_count[x])

        return sorted_nums[:k]



fun = Solution()

print(fun.topKFrequent(nums=[1,1,1,2,2,3], k=2))