# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('seaborn')

df_meal = pd.read_csv(r'C:\Users\lavin\Documents\Practising Python\AV_FoodDemandForecastingDataset\meal_info.csv') 
df_meal.head()

df_center = pd.read_csv(r'C:\Users\lavin\Documents\Practising Python\AV_FoodDemandForecastingDataset\fulfilment_center_info.csv') 
df_center.head()

df_food = pd.read_csv(r'C:\Users\lavin\Documents\Practising Python\AV_FoodDemandForecastingDataset\train.csv') 
df_food.head()


df = pd.merge(df_food,df_center,on='center_id') 
df = pd.merge(df,df_meal,on='meal_id')
df.to_csv("mergeddf.csv")

### Now df has basically allthe orders 

### 1. Bar Graph using matplotlib

table = pd.pivot_table(data=df,index='category',values='num_orders',aggfunc=np.sum)

#bar graph
plt.bar(table.index,table['num_orders'])

#xticks 
plt.xticks(rotation=70) 

#x-axis labels 
plt.xlabel('Food item') 

#y-axis labels 
plt.ylabel('Quantity sold') 

#plot title 
plt.title('Most popular food') 

#save plot 
plt.savefig(r'C:\Users\lavin\Documents\Practising Python\AV_FoodDemandForecastingDataset\matplotlib_plotting_6.png',dpi=300,bbox_inches='tight') 

plt.close()
#Let’s divide the total food item order by the number of unique meals it is present in.

#dictionary for meals per food item
item_count = {}

for i in range(table.index.nunique()):
    item_count[table.index[i]] = table.num_orders[i]/df_meal[df_meal['category']==table.index[i]].shape[0]

#bar plot 
plt.bar([x for x in item_count.keys()],[x for x in item_count.values()],color='orange')

#adjust xticks
plt.xticks(rotation=70)

#label x-axis
plt.xlabel('Food item')

#label y-axis
plt.ylabel('No. of meals')

#label the plot
plt.title('Meals per food item')

#save plot
plt.savefig(r'C:\Users\lavin\Documents\Practising Python\AV_FoodDemandForecastingDataset\matplotlib_plotting_7.png',dpi=300,bbox_inches='tight')

#display plot
plt.show()

### 2. Pie Chart 

#dictionary for cuisine and its total orders
d_cuisine = {}

#total number of order
total = df['num_orders'].sum()

#find ratio of orders per cuisine
for i in range(df['cuisine'].nunique()):

    #cuisine
    c = df['cuisine'].unique()[i]

    #num of orders for the cuisine
    c_order = df[df['cuisine']==c]['num_orders'].sum()
    d_cuisine[c] = c_order/total

#pie plot 
plt.pie([x*100 for x in d_cuisine.values()],labels=[x for x in d_cuisine.keys()],autopct='%0.1f',explode=[0,0,0.1,0]) 

#label the plot 
plt.title('Cuisine share %') 
#plt.savefig('C:\\Users\\Dell\\Desktop\\AV Plotting images\\matplotlib_plotting_8.png',dpi=300,bbox_inches='tight') 
plt.show();
plt.close()


###################### 3. plotting histogram 
plt.hist(df['base_price'],rwidth=0.9,alpha=0.3,color='blue',bins=15,edgecolor='red') 

#x and y-axis labels 
plt.xlabel('Base price range') 
plt.ylabel('Distinct order') 

#plot title 
plt.title('Inspecting price effect') 

#save and display the plot 
#plt.savefig('C:\\Users\\Dell\\Desktop\\AV Plotting images\\matplotlib_plotting_10.png',dpi=300,bbox_inches='tight') 
plt.show();