import pandas as pd
import numpy as np

## clean data in KY
#
# Usage: 
# $ python clean.py data/KY_Derby_Data1.csv results/clean.csv

KY1_df = pd.read_csv('data/KY_Derby_Data1.csv')
KY2_df = pd.read_csv('data/KY_Derby_Data2.csv')

# drop unneeded columns
KY1_df.drop(KY1_df.columns[8], axis =1, inplace=True)
#print(KY1_df.columns[8])
#print(KY1_df.head(1))

# replace all True/False with Yes/No
# Replace multiple values
KY1_df['triple_crown_winner'] = KY1_df['triple_crown_winner'].replace([True],'Yes')
KY1_df['triple_crown_winner'] = KY1_df['triple_crown_winner'].replace([False],'No')
#print(KY1_df)

pd.set_option('display.max_rows', None)
track_times = KY1_df[['track_condition','time_string']].sort_values(by = ['track_condition', 'time_string'], axis=0, ascending=[True, True], inplace=False)
track_times= track_times.groupby("track_condition").head(3)
#print(track_times)

#KY1_df_group = KY1_df.groupby("track_condition")
#KY1_df.group.get_group('Sloppy')
#print('track_condition')

#Adding a row for the earnings to prepare to drop the earnings row in the next step
KY2_df.loc[-1] = ['2022', '-', '-', '-']
KY2_df.index = KY2_df.index + 1  # shifting index
KY2_df.sort_index(inplace=True)

# Removes First Row of KY Derby file (since year 2022 is not on Data file 2)
KY1_df=KY1_df.drop(KY1_df.index[0])
earnings=KY2_df['Earnings']
KY1_df=KY1_df.join(earnings)
pd.set_option('display.max_rows', None)

#Replace NaN with NA
KY1_df['Earnings'] = KY1_df['Earnings'].fillna("-")
print(KY1_df)