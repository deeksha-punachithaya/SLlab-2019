import pandas as pd
import numpy as np

df = pd.read_csv("blackfri.csv")
df.head()

df.info()

df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'], axis=1, inplace=True)
df.head()

df['City_Category'] = df['City_Category'].fillna("A")
df.head()

df['City_Category'] = df['City_Category'].map({'A':'Metro cities','B':'Small Towns','C':'Villages'})
print(df.head(5))

df.rename(columns={'Product_Category_1':'Baseball_Caps','Product_Category_2':'Wine_Tumblers','Product_Category_3':'Pet_Raincoats'},inplace=True)
df.head(5)

import matplotlib.pyplot as plt
import seaborn as sns

print(pd.crosstab(df.Gender,df.Baseball_Caps))
print(pd.crosstab(df.Gender,df.Pet_Raincoats))

ax = sns.countplot(data=df,x='Gender',hue='Pet_Raincoats',palette='Set2')
ax.set(title='Male and Female who bought Pet_Raincoats',xlabel='Gender',ylabel='Count')
plt.show()

ax = sns.countplot(data=df,x='Gender',hue='City_Category',palette='Set1')
ax.set(title='Male and Female belonging to each city',xlabel='Gender',ylabel='Count')
plt.show()
