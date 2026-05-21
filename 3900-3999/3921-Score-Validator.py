class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score, counter = 0, 0
        for event in events:
            if event == 'W':
                counter += 1                    
            elif event == 'WD' or event == 'NB':
                score += 1
            else:
                score += int(event)

            if counter == 10:
                break

        return [score, counter]