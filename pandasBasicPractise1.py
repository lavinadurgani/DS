# -*- coding: utf-8 -*-

import pandas as pd

s = pd.Series([3 , -5 , 7 , 4] , index=['a' , 'b' , 'c' , 'd'])
print(s)

data = {'values': [3 , -5 , 7 , 4]}
s1 = pd.Series( data, dtype = int , index=['a' , 'b' , 'c' , 'd'])
print(s1)



data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data, orient='index')
print(df)
"""
       0  1  2  3
row_1  3  2  1  0
row_2  a  b  c  d
"""

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data)
print(df)
"""
   row_1 row_2
0      3     a
1      2     b
2      1     c
3      0     d
"""

data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame(data)
print(df)
"""
   row_1 row_2
0      3     a
1      2     b
2      1     c
3      0     d
"""

