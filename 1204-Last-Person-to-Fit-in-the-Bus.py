import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values(by='turn', ascending=True)
    queue['cumsum'] = queue['weight'].cumsum()
    return queue[queue['cumsum'] <= 1000].tail(1)[['person_name']]
