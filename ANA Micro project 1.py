#!/usr/bin/env python
# coding: utf-8

# Author: Ramon Rodriguez 
# 
# Date: 8/8/22

# In[2]:


import pandas as pd
import numpy as np


# In[2]:


import pandas as pd 
import numpy as np

url = "https://raw.githubusercontent.com/Ramon689/ANA-500/master/adult.data.csv"

df = pd.read_csv(url)


# In[3]:


df.head


# In[4]:


display(df)


# In[5]:


print(df.isnull().sum())


# In[14]:


mydata2=df.loc[~(df==0).all(axis=1)]


# In[15]:


print(myData2.isnull().sum())


# In[16]:


mydata2.describe()


# In[17]:


myData2.shape


# In[13]:





# In[ ]:




