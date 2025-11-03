# Pandas Solution for LeetCode 550: Game Play Analysis IV

import pandas as pd
from datetime import timedelta

Activity = pd.DataFrame({
    'player_id': [1, 1, 2, 3, 3],
    'device_id': [2, 2, 3, 1, 4],
    'event_date': pd.to_datetime(['2016-03-01', '2016-03-02', '2017-06-25', '2016-03-02', '2018-07-03']),
    'games_played': [5, 6, 1, 0, 5]
})

# Find first login date for each player
first_logins = Activity.groupby('player_id')['event_date'].min().reset_index()
first_logins.rename(columns={'event_date': 'first_login_date'}, inplace=True)
# Merge back to Activity
merged = Activity.merge(first_logins, on='player_id', how='left')
# Check if event_date is exactly one day after first_login_date
merged['day_after'] = merged['first_login_date'] + timedelta(days=1)
players_retained = merged[merged['event_date'] == merged['day_after']]
# Calculate fraction
num_retained = players_retained['player_id'].nunique()
total_players = Activity['player_id'].nunique()
fraction = round(num_retained / total_players, 2)

result = pd.DataFrame({'fraction': [fraction]})
print(result)

