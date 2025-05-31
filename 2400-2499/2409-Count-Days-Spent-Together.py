class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def date_to_days(date: str) -> int:
            month, day = map(int, date.split('-'))
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return sum(days_in_month[:month-1]) + day
        
        alice_arrive = date_to_days(arriveAlice)
        alice_leave = date_to_days(leaveAlice)
        bob_arrive = date_to_days(arriveBob)
        bob_leave = date_to_days(leaveBob)
        
        overlap_start = max(alice_arrive, bob_arrive)
        overlap_end = min(alice_leave, bob_leave)
        
        return max(0, overlap_end - overlap_start + 1)