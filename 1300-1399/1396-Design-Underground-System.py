class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check_ins[id]
        route = (startStation, stationName)
        travel_time = t - startTime

        if route not in self.travel_times:
            self.travel_times[route] = [travel_time, 1]
        else:
            self.travel_times[route][0] += travel_time
            self.travel_times[route][1] += 1

        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count
