from collections import deque, defaultdict
import bisect

class Router:

    def __init__(self, memory_limit: int):
        self.memory_limit = memory_limit
        self.queue = deque()
        self.packets_set = set()
        self.dest_timestamps = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packets_set:
            return False

        if len(self.queue) >= self.memory_limit:
            old_src, old_dst, old_time = self.queue.popleft()
            self.packets_set.remove((old_src, old_dst, old_time))
            timestamps = self.dest_timestamps[old_dst]
            idx = bisect.bisect_left(timestamps, old_time)
            if idx < len(timestamps) and timestamps[idx] == old_time:
                timestamps.pop(idx)

        self.queue.append((source, destination, timestamp))
        self.packets_set.add(key)

        bisect.insort(self.dest_timestamps[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []

        src, dst, time = self.queue.popleft()
        self.packets_set.remove((src, dst, time))
        timestamps = self.dest_timestamps[dst]
        idx = bisect.bisect_left(timestamps, time)
        if idx < len(timestamps) and timestamps[idx] == time:
            timestamps.pop(idx)

        return [src, dst, time]

    def getCount(self, destination: int, start_time: int, end_time: int) -> int:
        timestamps = self.dest_timestamps.get(destination, [])
        left = bisect.bisect_left(timestamps, start_time)
        right = bisect.bisect_right(timestamps, end_time)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
