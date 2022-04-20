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
print(df.iloc[0])
"""
Country        Belgium
Capital       Brussels
Population    11190846
Name: 0, dtype: object
"""
print(df.iloc[[0]])
"""
   Country   Capital  Population
0  Belgium  Brussels    11190846
"""

print(df.iloc[[0][0]])
"""
Country        Belgium
Capital       Brussels
Population    11190846
Name: 0, dtype: object
"""

print(df.iloc[[0][0]][0])
"""Belgium"""

print(df.iloc[[0] , [0]])
"""
   Country
0  Belgium
"""

print(df.loc[2])
"""
Country          Brazil
Capital        Brasilia
Population    207847528
Name: 2, dtype: object
"""

print(df.loc[2 , 'Country'])
"""
Brazil
"""

print(df.iloc[[2][0]])
"""
Country          Brazil
Capital        Brasilia
Population    207847528
Name: 2, dtype: object
"""

print(df.iloc[[2][0]][0])
"""
Brazil
"""


#################################################
"""
Select row labels to “10” and “InternetService” and “PhoneService” columns of customer with a Partner (Partner == ‘Yes’)

We filter the dataframe but do not change the index. Thus, the indices of the resulting dataframe only contain the labels of the rows that are not omitted. Therefore, when use loc[:10], we can select the rows with labels up to “10”. O the other hand, if we use iloc[:10] after applying the filter, we get 10 rows because iloc selects by position regardless of the labels.

As you notice, we also need to change the way to select the columns. We also need to pass the positions of columns to iloc.

"""





