#!/usr/bin/env python
# coding: utf-8

# Author: Ramon Rodriguez
# 
# 

# In[156]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import requests

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/Ramon689/ANA-500/master/adult.data.csv"

myData = pd.read_csv(url, index_col=0)


# In[157]:



myData.info()

myData.head()


# In[158]:


print(myData.isnull().sum())


# In[159]:


myData.duplicated()


# In[160]:


mydata.columns


# In[161]:


myData2=myData.dropna(axis =0, how='any', thresh =None, subset = None, inplace = False)


# In[162]:


print(myData2.isnull().sum())


# In[163]:


myData2.shape


# In[164]:


myData2.columns


# In[135]:



x = myData2.loc[:,'Income']

fig, axs = plt.subplots(1, 1,
                        figsize =(12, 10),
                        tight_layout = True)
axs.hist(x, bins = 2)


plt.grid(axis='y', linestyle ='-.', linewidth = 2, color ='red', alpha=0.5)
plt.xlabel('Income')
plt.ylabel('Counts')
plt.title('Income Distribution')
plt.show()


# In[151]:




sns.boxplot(data=myData2, x='Age', y = 'Income').set(title='Income by Education')


# In[149]:



sns.lineplot(data=myData2, x='Race', y = 'Education', style= 'Income').set(title='Education vs Race')


# In[137]:


sns.lineplot(data=myData2, x='<', y = 'Income').set(title='Income vs Education')


# In[91]:


sns.boxplot(data=myData2, x='Age', y = 'Income', hue='Race').set(title='Income vs Age')


# In[169]:


fig, ax = plt.subplots()

sns.catplot('Race', hue='Income', data=myData2, kind='count', 
            palette={1:'blue', 0:'green'}, ax=ax)

plt.close(2) # catplot creates an extra figure we don't need

ax.set_xlabel('Race')

color_patches = [
    Patch(facecolor="blue", label="<50k"),
    Patch(facecolor="green", label=">50k")
]
ax.legend(handles=color_patches)

fig.suptitle("Race vs. SRace2");


# In[172]:


fig, ax = plt.subplots()

sns.catplot("Income", hue="Race", data=myData2, kind="count", 
            palette={1:"yellow", 2:"orange"}, ax=ax)

plt.close(2) # catplot creates an extra figure we don't need

ax.legend(title="Income")
ax.set_xticklabels(["<=50k", ">50k"])
ax.set_xlabel("")

fig.suptitle("Passenger Class vs. Survival for Titanic Passengers");


# In[173]:


from sklearn.cluster import KMeans
BOW_kmeans = KMeans(n_clusters=5, max_iter=100).fit(BOW_train)


# In[ ]:




