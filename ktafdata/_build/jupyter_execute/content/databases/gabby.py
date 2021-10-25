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


#Regular pandas view of the all columns/tables view of the database (First 100 entries)
columns_df.head(100)


# QGrid is a tool that creates a sortable widget on a dataframe, but we need to configure it to run on Jupyter Notebook.

# In[4]:


# Qgrid view

widget = qgrid.show_grid(columns_df)
widget


# PivotTable.js is an open-source Javascript Pivot Table (aka Pivot Grid, Pivot Chart, Cross-Tab) implementation with drag'n'drop functionality

# In[5]:


#Pivottablejs view
pivot_ui(columns_df, outfile_path='pivottablejs.html')
HTML('pivottablejs.html')


# Below is just an embedded Google Sheet of the All Columns/All Tables view [here](https://docs.google.com/spreadsheets/d/1i77SNKkU8xHyDECKo_YWZh_lEIKJtnd3O6vJNtjNcUA/edit?usp=sharing)

# <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTyB4iCoIqMbBsYGIHfL7fy95To5jHqsK0mrbcthmVBYSaAZiyVIJ3M56dMb27FnL2Pi8gDGxEQhHNq/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=true"></iframe>
