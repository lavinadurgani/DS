# -*- coding: utf-8 -*-
"""
A very high level difference is that 
merge() is used to combine two (or more) dataframes on the basis of values of common columns (indices can also be used, use left_index=True and/or right_index=True), 
concat() is used to append one (or more) dataframes one below the other (or sideways, depending on whether the axis option is set to 0 or 1).

join() is used to merge 2 dataframes on the basis of the index; instead of using merge() with the option left_index=True we can use join().


"""
import pandas as pd 

######################### CONACT, AXIS =0 ###################

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)
df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)


frames = [df1, df2, df3] # Frames is a list of Dataframes to be concateneted


result = pd.concat(frames , axis = 0) # Axis 0 is one below the other , needs the columns to be same in number.
print(result)
"""
      A    B    C    D
0    A0   B0   C0   D0
1    A1   B1   C1   D1
2    A2   B2   C2   D2
3    A3   B3   C3   D3
4    A4   B4   C4   D4
5    A5   B5   C5   D5
6    A6   B6   C6   D6
7    A7   B7   C7   D7
8    A8   B8   C8   D8
9    A9   B9   C9   D9
10  A10  B10  C10  D10
11  A11  B11  C11  D11
"""

result2 = pd.concat(frames, keys=["x", "y", "z"])

"""
        A    B    C    D
x 0    A0   B0   C0   D0
  1    A1   B1   C1   D1
  2    A2   B2   C2   D2
  3    A3   B3   C3   D3
y 4    A4   B4   C4   D4
  5    A5   B5   C5   D5
  6    A6   B6   C6   D6
  7    A7   B7   C7   D7
z 8    A8   B8   C8   D8
  9    A9   B9   C9   D9
  10  A10  B10  C10  D10
  11  A11  B11  C11  D11
 """

print(result2.loc["y"])
"""

    A   B   C   D
4  A4  B4  C4  D4
5  A5  B5  C5  D5
6  A6  B6  C6  D6
7  A7  B7  C7  D7

"""

############## CONCAT , AXIS = 1 #################

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)
df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)

result3 = pd.concat([df1, df4], axis=1 , join = "outer") ### OUTER JOIN 
print(result3)
"""
     A    B    C    D    B    D    F
0   A0   B0   C0   D0  NaN  NaN  NaN
1   A1   B1   C1   D1  NaN  NaN  NaN
2   A2   B2   C2   D2   B2   D2   F2
3   A3   B3   C3   D3   B3   D3   F3
6  NaN  NaN  NaN  NaN   B6   D6   F6
7  NaN  NaN  NaN  NaN   B7   D7   F7
"""

result4 = pd.concat([df1, df4], axis=1 , join = "inner") ### INNER JOIN 
print(result4)
"""
   A   B   C   D   B   D   F
2  A2  B2  C2  D2  B2  D2  F2
3  A3  B3  C3  D3  B3  D3  F3
"""


######################### MERGE #########################



df1 = pd.DataFrame({'Key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
"""
df1:
   Key  data1
0   b   0
1   b   1
2   a   2
3   c   3
4   a   4
5   a   5
6   b   6
"""
df2 = pd.DataFrame({'Key': ['a', 'b', 'd'], 'data2': range(3)})
"""
df2:
    Key data2
0   a   0
1   b   1
2   d   2
"""

#Merge
# The 2 dataframes are merged on the basis of values in column "Key" as it is 
# a common column in 2 dataframes

pd.merge(df1, df2)
"""
   Key data1 data2
0   b    0    1
1   b    1    1
2   b    6    1
3   a    2    0
4   a    4    0
5   a    5    0
"""

############# JOIN ######################


df_joined = pd.join(df1, df2)

print(df_joined)


########## CONCLUSION ###############
"""
.merge() can only use columns (plus row-indices) and it is semantically suitable for database-style operations. .concat() can be used with either axis, using only indices, and gives the option for adding a hierarchical index.

Incidentally, this allows for the following redundancy: both can combine two dataframes using the rows indices.

pd.DataFrame.join() merely offers a shorthand for a subset of the use cases of .merge()
"""

"""
.concat() simply stacks multiple DataFrame together either vertically, or stitches horizontally after aligning on index
.merge() first aligns two DataFrame' selected common column(s) or index, and then pick up the remaining columns from the aligned rows of each DataFrame.
More specifically, .concat():

Is a top-level pandas function
Combines two or more pandas DataFrame vertically or horizontally
Aligns only on the index when combining horizontally
Errors when any of the DataFrame contains a duplicate index.
Defaults to outer join with the option for inner join
And .merge():

Exists both as a top-level pandas function and a DataFrame method (as of pandas 1.0)
Combines exactly two DataFrame horizontally
Aligns the calling DataFrame's column(s) or index with the other DataFrame's column(s) or index
Handles duplicate values on the joining columns or index by performing a cartesian product
Defaults to inner join with options for left, outer, and right
Note that when performing pd.merge(left, right), if left has two rows containing the same values from the joining columns or index, each row will combine with right's corresponding row(s) resulting in a cartesian product. On the other hand, if .concat() is used to combine columns, we need to make sure no duplicated index exists in either DataFrame.

Practically speaking:

Consider .concat() first when combining homogeneous DataFrame, while consider .merge() first when combining complementary DataFrame.
If need to merge vertically, go with .concat(). If need to merge horizontally via columns, go with .merge(), which by default merge on the columns in common.
"""