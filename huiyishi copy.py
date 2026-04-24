def num_room(intervals):
    if not intervals:
        return 0
    intervals.sort(key = lambda p:p[0])
    import heapq

    freeRoom = []

    heapq.heappush(freeRoom, intervals[0][1])

    for s in intervals[1:]:
        if s[0]>=freeRoom[0]:
            heapq.heappop(freeRoom)
        heapq.heappush(freeRoom, s[1])
    return len(freeRoom)