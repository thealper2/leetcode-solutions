import bisect


class TimeMap:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_time_map:
            self.key_time_map[key] = {'values': [], 'timestamps': []}
        
        self.key_time_map[key]['timestamps'].append(timestamp)
        self.key_time_map[key]['values'].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_time_map:
            return ""
        
        timestamps = self.key_time_map[key]['timestamps']
        values = self.key_time_map[key]['values']
        idx = bisect.bisect_right(timestamps, timestamp) - 1
        
        if idx < 0:
            return ""
        
        return values[idx]