#!/usr/bin/env python
# coding: utf-8

# # Assessing
# 
# We using pandas to explore all_alpha_08.csv and all_alpha_18.csv datasets in the Jupyter Notebook to answer the below characteristics of the data:
# 
# - number of samples in each dataset
# - number of columns in each dataset
# - duplicate rows in each dataset
# - datatypes of columns
# - features with missing values
# - number of non-null unique values for features in each dataset 
# - what those unique values are and counts for each

# In[1]:


#import libraries  
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#import files
df_08 = pd.read_csv('all_alpha_08.csv')
df_18 = pd.read_csv('all_alpha_18.csv')


# In[29]:


#review dataset shape
df_08.shape


# In[30]:


#review dataset shape
df_18.shape


# In[3]:


#review the dataset
df_08.head()


# In[4]:


#review the dataset
df_18.head()


# In[5]:


#check the dublicated rows sum
sum(df_08.duplicated())


# In[6]:


#review the data types and info
df_08.info()


# In[18]:


#review the data types and info
df_18.info()


# In[21]:


# review dataset on histograms
df_08.hist(figsize=(15,8));


# In[20]:


# review dataset on histograms
df_18.hist(figsize=(15,8));


# In[23]:


# check null values of the dataframe
df_08.isnull().sum()


# In[24]:


# check null values of the dataframe
df_18.isnull().sum()


# In[31]:


# review summary of dataset
df_08.describe()


# In[32]:


# review summary of dataset
df_18.describe()

