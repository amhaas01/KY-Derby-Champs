import pandas as pd
import numpy as np

## clean data in KY-Derby_Data1.csv (from Kaggle)
#
# Usage: 
# $ python clean.py data/KY_Derby_Data1.csv results/clean.csv

# where:
#  KY_Derby_Data1.csv    = C:\Users\ahaas.SDDOMAIN\Desktop\KY-Derby-Champs\data
#  clean.csv             = C:\Users\ahaas.SDDOMAIN\Desktop\KY-Derby-Champs\results

# Read in Data files
KY1_df = pd.read_csv('data/KY_Derby_Data1.csv')
KY2_df = pd.read_csv('data/KY_Derby_Data2.csv')

# drop unneeded columns
KY1_df.drop(KY1_df.columns[7], axis =1, inplace=True)

# replace all True/False with Yes/No
KY1_df['triple_crown_winner'] = KY1_df['triple_crown_winner'].replace([True],'Yes')
KY1_df['triple_crown_winner'] = KY1_df['triple_crown_winner'].replace([False],'No')

# Adding a row for the earnings to prepare to drop the earnings row in the next step
KY2_df.loc[-1] = ['2022', '-', '-', '-']
KY2_df.index = KY2_df.index + 1  # shifting index
KY2_df.sort_index(inplace=True)

#remove $ sign from Earnings column (to later convert string to int or float)
KY2_df['Earnings']=KY2_df['Earnings'].str.slice(1,20)

# Removes First Row of KY Derby file (since year 2022 is not on Data file 2)
KY1_df=KY1_df.drop(KY1_df.index[0])
earnings=KY2_df['Earnings']
KY1_df=KY1_df.join(earnings)
pd.set_option('display.max_rows', None)

#Replace NaN with NA
KY1_df['Earnings'] = KY1_df['Earnings'].fillna("-")

#If I want to drop years prior to 1930
#KY1_df = KY1_df[KY1_df.Earnings.notnull()]
KY1_df=KY1_df[KY1_df.distance != 1.5]

KY1_df.rename(columns = {'winner':'Winner', 'jockey':'Jockey', 'owner':'Owner', 'distance':'Distance', 'trainer':'Trainer', 'triple_crown_winner':'Triple Crown Winner', 'track_condition':'Track Condition', 'year':'Year', 'time_sec':'Time (Sec)'}, inplace = True)
KY1_df.to_csv('results/clean.csv')