class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #枚举法 O(n^2)，O(1)
        # n = len(intervals)
        # ans = n
        # for i in range(n):
        #     for j in range(n):
        #         if i!=j and intervals[j][0]<=intervals[i][0] and intervals[j][1]>=intervals[i][1]:
        #             ans -= 1
        #             break
        # return ans

        #O(NlogN)、O(logN)
        n = len(intervals)
        intervals.sort(key = lambda u:(u[0], -u[1]))
        cnt = len(intervals)
        rmax = intervals[0][1]

        for i in range(1, n):
            if intervals[i][1] <= rmax:
                cnt -= 1
            else:
                rmax = intervals[i][1]
        return cnt
