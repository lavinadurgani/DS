# -*- coding: utf-8 -*-

import pandas as pd
studentsPerformanceDataDF = pd.read_csv(r'C:\Users\lavin\Documents\Practising Python\Kaggle_StudentsPerformanceDataset\StudentsPerformance.csv')

print(studentsPerformanceDataDF.head()) ## can also do tail()

print(studentsPerformanceDataDF.shape) ## (1000, 8)


print(studentsPerformanceDataDF.columns)
"""
Index(['gender', 'race/ethnicity', 'parental level of education', 'lunch',
       'test preparation course', 'math score', 'reading score',
       'writing score'],
      dtype='object')
"""

print(studentsPerformanceDataDF.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 8 columns):
 #   Column                       Non-Null Count  Dtype 
---  ------                       --------------  ----- 
 0   gender                       1000 non-null   object
 1   race/ethnicity               1000 non-null   object
 2   parental level of education  1000 non-null   object
 3   lunch                        1000 non-null   object
 4   test preparation course      1000 non-null   object
 5   math score                   1000 non-null   int64 
 6   reading score                1000 non-null   int64 
 7   writing score                1000 non-null   int64 
dtypes: int64(3), object(5)
memory usage: 62.6+ KB
"""
print(studentsPerformanceDataDF.ndim) ### 2 - Dataframe

print(studentsPerformanceDataDF.describe())
"""
       math score  reading score  writing score
count  1000.00000    1000.000000    1000.000000
mean     66.08900      69.169000      68.054000
std      15.16308      14.600192      15.195657
min       0.00000      17.000000      10.000000
25%      57.00000      59.000000      57.750000
50%      66.00000      70.000000      69.000000
75%      77.00000      79.000000      79.000000
max     100.00000     100.000000     100.000000
"""

print(studentsPerformanceDataDF.sample())

print(studentsPerformanceDataDF.isnull( ).sum( ))
"""
gender                         0
race/ethnicity                 0
parental level of education    0
lunch                          0
test preparation course        0
math score                     0
reading score                  0
writing score                  0
dtype: int64
"""


print(studentsPerformanceDataDF.nunique( ))
"""
gender                          2
race/ethnicity                  5
parental level of education     6
lunch                           2
test preparation course         2
math score                     81
reading score                  72
writing score                  77
dtype: int64
"""


print(studentsPerformanceDataDF.std( ))
"""
math score       15.163080
reading score    14.600192
writing score    15.195657
dtype: float64
"""
print(studentsPerformanceDataDF.mode( ))
"""
   gender race/ethnicity  ... reading score writing score
0  female        group C  ...            72            74
"""

"""
This article was published as a part of the Data Science Blogathon.
Introduction
Exploratory Data Analysis(EDA) is an important component as well as one of the most under-estimated steps in any Data Science project. EDA is essential for well-defined and structured data analysis and should be performed before the machine learning modeling phase.

It involves finding insights from the data upon careful observation and further summarizing its main characteristics. Generally, the real-life data which we work upon contains a lot of ‘noise’, and therefore performing data analysis manually on such datasets becomes a complicated and tedious process.

EDA Pandas
Python Getting Started Tutorial: Scientific Calculation with Pandas | by Data Analysis Enthusiast | Medium

Python is one of the most widely used languages for Data Science particularly because of the presence of various libraries and packages that makes data analysis easier.

Accordingly, Pandas is one of the most popular libraries of Python that helps to present the data in a way which is suitable for analysis via its Series and DataFrame data structures. It provides various functions and methods to both simplify as well as expedite the data analysis process.

Here we use  “TITANIC” Dataset to do the practical implementation of all functions.

 

Firstly, we import Numpy and pandas library and then read the dataset.

import Numpy and pandas EDA

 
Now Let’s Get Started
 

1. df.head( ): By default, it returns the first 5 rows of the Dataframe. To change the default, you may insert a value between the parenthesis to change the number of rows returned.

head  pandas eda

2. df.tail( ): By default, it returns the last 5 rows of the Dataframe. This function is used to get the last n rows. This function returns the last n rows from the object based on position.

tail pandas

3. df.info( ): It helps in getting a quick overview of the dataset. This function is used to get a brief summary of the dataframe. This method prints information about a DataFrame including the index dtype and column dtypes, non-null values, and memory usage.

info pandas

4. df.shape: It shows the number of dimensions as well as the size in each dimension. Since data frames are two-dimensional, what shape returns is the number of rows and columns.

shape pandas

5. df.size: Return an int representing the number of elements in this object. Return the number of rows if Series, otherwise returns the number of rows times the number of columns if DataFrame.

size pandas

6. df.ndim: Returns dimension of dataframe/series. 1 for one dimension (series), 2 for two dimensions (dataframe).

ndim pandas

7. df.describe( ): Return a statistical summary for numerical columns present in the dataset. This method calculates some statistical measures like percentile, mean and standard deviation of the numerical values of the Series or DataFrame.

describe

8. df.sample( ): Used to generate a sample randomly either row or column. It allows you to select values randomly from a Series or DataFrame. It is useful when we want to select a random sample from a distribution.

sample

9. df.isnull( ).sum( ): Return the number of missing values in each column.

isnull

10. df.nunique( ): Return number of unique elements in the object. It counts the number of unique entries over columns or rows. It is very useful in categorical features especially in cases where we do not know the number of categories beforehand.

nunique

11. df.index: This function searches for a given element from the start of the list and returns the lowest index where the element appears.

index

12. df.columns: Return the column labels of the dataframe.

columns

13. df.memory_usage( ): Returns how much memory each column uses in bytes. It is useful especially when we work with large data frames.

memory_usage

14. df.dropna( ): This function is used to remove a row or a column from a dataframe that has a NaN or missing values in it.

dropna

15. df.nlargest( ): Returns the first n rows ordered by columns in descending order.

nlargest

16. df.isna( ): This function returns a dataframe filled with boolean values with true indicating missing values.

isna

 

17. df.duplicated( ):  Returns a boolean Series denoting duplicate rows.

duplicated

18. value_counts( ): This function is used to get a Series containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently occurring element. It excludes missing values by default. This function comes in handy when we want to check the problem of class imbalance for a categorical variable.

value_counts

19. df.corr( ): This function is used to find the pairwise correlation of all columns in the dataframe. Any missing values are automatically excluded. For any non-numeric data type columns in the dataframe, it is ignored. This function comes in handy while we doing the Feature Selection by observing the correlation between features and target variable or between variables.

corr

20. df.dtypes: This function shows the data type of each column.

"""
import seaborn as sns
x=studentsPerformanceDataDF['gender'].value_counts()
print(x)
sns.barplot(x.index,x)
#sns.close()
sns.countplot(x = 'race/ethnicity' , hue = 'gender' , data = studentsPerformanceDataDF )
"""
female    518
male      482
"""

print(studentsPerformanceDataDF.isna().sum())
"""
gender                         0
race/ethnicity                 0
parental level of education    0
lunch                          0
test preparation course        0
math score                     0
reading score                  0
writing score                  0
dtype: int64
"""


