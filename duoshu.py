import collections
def duoshu(nums):
    counts = collections.Counter(nums)
    print(counts.keys())
    print(counts.items())
    max_count = 0
    target = None
    for num, cnt in counts.items():
        if cnt>max_count:
            target = num
            max_count = cnt
    print(target)

    ans = max(counts.keys(), key=counts.get)

duoshu([2,2,1,1,1,2,2])