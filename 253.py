import heapq

def minMeetingRooms(intervals):
    # 如果会议安排列表为空，直接返回0
    if not intervals:
        return 0
    
    # 初始化一个空的最小堆
    free_rooms = []
    
    # 先根据会议的开始时间对会议进行排序
    intervals.sort(key=lambda x: x[0])
    
    # 将第一个会议的结束时间加入到最小堆中
    # 这表示目前我们有一个会议室被占用，直到这个时间点
    heapq.heappush(free_rooms, intervals[0][1])
    
    # 从第二个会议开始遍历
    for i in intervals[1:]:
        # 如果当前会议的开始时间大于等于最小堆中的最早结束时间
        # 说明这个会议室可以被重复使用
        # 因此我们可以移除堆顶元素（最早结束的会议室）
        if i[0] >= free_rooms[0]:
            heapq.heappop(free_rooms)
        # 将当前会议的结束时间加入最小堆
        # 表示新增一个会议室，或是延续使用原会议室
        heapq.heappush(free_rooms, i[1])
    # 堆中元素的数量，就是我们需要的会议室数量
    return len(free_rooms)