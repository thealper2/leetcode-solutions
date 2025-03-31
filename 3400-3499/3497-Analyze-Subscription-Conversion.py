import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    trial_activities = user_activity[user_activity['activity_type'] == 'free_trial']
    paid_activities = user_activity[user_activity['activity_type'] == 'paid']
    
    trial_avg = trial_activities.groupby('user_id')['activity_duration'].mean().add(0.0001).round(2)
    paid_avg = paid_activities.groupby('user_id')['activity_duration'].mean().add(0.0001).round(2)
    
    result = pd.DataFrame({
        'trial_avg_duration': trial_avg,
        'paid_avg_duration': paid_avg
    }).reset_index()
    
    return result.sort_values('user_id').dropna()