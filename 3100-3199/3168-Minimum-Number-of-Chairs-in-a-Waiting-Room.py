class Solution:
    def minimumChairs(self, s: str) -> int:
        max_people = 0
        current_people = 0

        for event in s:
            if event == 'E':
                current_people += 1
            
            elif event == 'L':
                current_people -= 1

            max_people = max(max_people, current_people)

        return max_people