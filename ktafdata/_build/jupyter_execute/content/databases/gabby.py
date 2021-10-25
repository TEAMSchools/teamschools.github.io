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
import qgrid
import tabloo
from pivottablejs import pivot_ui
from IPython.display import HTML


# In[2]:


file = 'all_columns.csv'
columns_df=pd.read_csv(file)


# In[3]:


#Regular pandas view of all the data
columns_df


# In[4]:


#Qgrid view

# widget = qgrid.show_grid(columns_df)
# widget


# In[5]:


#Pivottablejs view
pivot_ui(columns_df, outfile_path='pivottablejs.html')
HTML('pivottablejs.html')


# <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTyB4iCoIqMbBsYGIHfL7fy95To5jHqsK0mrbcthmVBYSaAZiyVIJ3M56dMb27FnL2Pi8gDGxEQhHNq/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false"></iframe>
