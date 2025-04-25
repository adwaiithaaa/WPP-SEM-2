import pandas as pd

data = {'day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10'],
        'john': [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        'judy': [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]}

df = pd.DataFrame(data)

df['party'] = (df['john'] & df['judy'])

df['days_til_party'] = df['party'][::-1].cumsum()[::-1]
df['days_til_party'] = df['days_til_party'].replace({1: 0}).fillna(method='bfill')

print(df)