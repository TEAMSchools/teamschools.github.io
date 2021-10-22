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
import pivottablejs


# In[2]:


file = 'all_columns.csv'
columns_df=pd.read_csv(file)


# In[3]:


#Regular pandas view of all the data
columns_df


# In[4]:


#Sortable/searchable list with qgrid
qgrid.QgridWidget(df=columns_df)
qgrid


# In[ ]:




