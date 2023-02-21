import pandas as pd


def prepare_weather(filename, year):
    initial_df = pd.read_csv(f'data/{filename}', header=0)
    initial_df['day'] = initial_df[year]
    initial_df.drop([year], inplace=True, axis=1)
    s = pd.DataFrame(initial_df.set_index(['day']).unstack(['day']))
    df = pd.DataFrame(s.to_records(), index=s.index).reset_index(drop=True)[['level_0', 'day', '0']].reset_index(drop=True)
    df['date'] = df['day'].astype(str) + "-" + df['level_0'] + f'-{year}'
    df = df[['0', 'date']].dropna()
    df['date'] = pd.to_datetime(df['date'])
    return df