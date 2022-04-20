# -*- coding: utf-8 -*-

import pandas as pd 

data = {'Country': ['Belgium',  'India',  'Brazil'],

'Capital': ['Brussels',  'New Delhi',  'Brasilia'],

'Population': [11190846, 1303171035, 207847528]} 

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])

"""
loc: select by labels of rows and columns
iloc: select by positions of rows and columns
"""

print(df)
"""
   Country    Capital  Population
0  Belgium   Brussels    11190846
1    India  New Delhi  1303171035
2   Brazil   Brasilia   207847528
"""


print(df.drop('Country', axis=1) )
"""
     Capital  Population
0   Brussels    11190846
1  New Delhi  1303171035
2   Brasilia   207847528
"""
print(df.drop([1]))
"""
   Country   Capital  Population
0  Belgium  Brussels    11190846
2   Brazil  Brasilia   207847528
"""

print(df.sort_index())
"""
   Country    Capital  Population
0  Belgium   Brussels    11190846
1    India  New Delhi  1303171035
2   Brazil   Brasilia   207847528
"""

print(df.sort_values(by='Country') )
"""
   Country    Capital  Population
0  Belgium   Brussels    11190846
2   Brazil   Brasilia   207847528
1    India  New Delhi  1303171035
"""
print(df.rank())
"""
   Country  Capital  Population
0      1.0      2.0         1.0
1      3.0      3.0         3.0
2      2.0      1.0         2.0
"""
print(df.shape) ##### (3, 3)
print(df.index) #### RangeIndex(start=0, stop=3, step=1)
print(df.columns) ### Index(['Country', 'Capital', 'Population'], dtype='object')
print(df.info()) ###
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   Country     3 non-null      object
 1   Capital     3 non-null      object
 2   Population  3 non-null      int64 
dtypes: int64(1), object(2)
memory usage: 200.0+ bytes
None
"""

print(df.count()) ###
"""
Country       3
Capital       3
Population    3
dtype: int64
"""

print(df.sum())
"""
Country              BelgiumIndiaBrazil
Capital       BrusselsNew DelhiBrasilia
Population                   1522209409
dtype: object
"""

print(df.cumsum())
"""
              Country                    Capital  Population
0             Belgium                   Brussels    11190846
1        BelgiumIndia          BrusselsNew Delhi  1314361881
2  BelgiumIndiaBrazil  BrusselsNew DelhiBrasilia  1522209409
"""

print(df.min())
"""
Country        Belgium
Capital       Brasilia
Population    11190846
dtype: object
"""
print(df.max())
"""
Country            India
Capital        New Delhi
Population    1303171035
dtype: object
"""


print(df.mean())
"""
Population    5.074031e+08
dtype: float64
"""

print(df.median())
"""
Population    207847528.0
dtype: float64

"""
f = lambda x: (x*2)
print(df.apply(f))
"""
          Country             Capital  Population
0  BelgiumBelgium    BrusselsBrussels    22381692
1      IndiaIndia  New DelhiNew Delhi  2606342070
2    BrazilBrazil    BrasiliaBrasilia   415695056
"""
print(df.applymap(f))
"""
          Country             Capital  Population
0  BelgiumBelgium    BrusselsBrussels    22381692
1      IndiaIndia  New DelhiNew Delhi  2606342070
2    BrazilBrazil    BrasiliaBrasilia   415695056
"""


s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
s3 = pd.Series([7, -2, 3],  index=['a',  'c',  'd'])

print(s)
"""
a    3
b   -5
c    7
d    4

"""
print(s3)
"""
dtype: int64
a    7
c   -2
d    3
"""
print(s+s3)
"""
dtype: int64
a    10.0
b     NaN
c     5.0
d     7.0
"""

print(s.add(s3 , fill_value = 0))

"""
a    10.0
b    -5.0
c     5.0
d     7.0
"""
print(s.sub(s3 , fill_value = 0))
"""
a   -4.0
b   -5.0
c    9.0
d    1.0
dtype: float64
"""
print(s.mul(s3 , fill_value = 0))
"""
dtype: float64
a    21.0
b    -0.0
c   -14.0
d    12.0
"""
print(s.div(s3 , fill_value = 0))
"""
a    0.428571
b        -inf
c   -3.500000
d    1.333333
dtype: float64
"""



