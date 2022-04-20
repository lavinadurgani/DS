# -*- coding: utf-8 -*-
import pandas as pd

train_df = pd.read_csv(r'preprocessed.csv')
train_df.head()

print(train_df.head())

print(train_df.columns)
"""
Index(['Unnamed: 0', 'Id', 'Comment', 'Topic', 'ContractionsRemoved',
       'Tokens_NoStopWords', 'stemmed_Tokens'],
      dtype='object')
"""
print(train_df.shape) # (8695, 7)

print(train_df['Topic'].value_counts())
"""
Biology      3591
Chemistry    2920
Physics      2184
Name: Topic, dtype: int64
"""

print(train_df.describe())
"""
count  8695.000000
mean   4347.000000
std    2510.174629
min       0.000000
25%    2173.500000
50%    4347.000000
75%    6520.500000
max    8694.000000
"""
