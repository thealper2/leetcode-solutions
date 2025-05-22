import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    ip_counts = logs.groupby('ip', as_index=False).size().reset_index(drop=True)
    invalid_ips = ip_counts[~ip_counts['ip'].str.contains(ipv4_pattern, regex=True)]
    invalid_ips = invalid_ips.rename(columns={'size': 'invalid_count'})
    invalid_ips = invalid_ips.sort_values(['invalid_count', 'ip'], ascending=[False, False])
    return invalid_ips