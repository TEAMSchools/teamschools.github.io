#!/usr/bin/env python
# coding: utf-8

# # Databases: Gabby
# 
# Gabby stores KTAF Student, Alumni, and People Data in a SQL Server. Below we'll include a searchable list of fields, tables, and views.
# 

# 

# In[1]:


#Sortable dataframe tools
import pandas as pd
# import qgrid
# import ipywidgets
from pivottablejs import pivot_ui
from IPython.display import HTML


# In[2]:


file = 'all_columns.csv'
columns_df=pd.read_csv(file)


# In[3]:


#Regular pandas view of all the data
columns_df


# In[4]:


df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]})
df


# In[5]:


pivot_ui(columns_df, outfile_path='pivottablejs.html')
HTML('pivottablejs.html')


# In[ ]:




