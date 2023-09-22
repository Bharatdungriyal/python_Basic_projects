#!/usr/bin/env python
# coding: utf-8

# 
# # Weather Data Analysis

# 
# *** Here, The Weather Dataset is a time-series data set with per-hour information about the weather conditions at a particular location. It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure, and Conditions.
# 
# 
# This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame.

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


Data = pd.read_csv(r"C:\Users\HP\Downloads\Project+1+-+Weather+Dataset (1).csv")


# In[21]:


Data.head() # It shows the first N rows in the data (by default, N=5).


# In[4]:


Data.shape # It shows the total no. of rows and no. of columns of the dataframe


# In[5]:


Data.index  # This attribute provides the index of the dataframe


# In[7]:


Data.columns 


# In[9]:


Data.dtypes    #   It shows the data-type of each column 


# In[24]:


Data['Weather'].unique()     #In a column, it shows all the unique values. 
# It can be applied on a single column only, not on the whole dataframe.


# In[12]:


Data["Weather"].nunique()   


# In[13]:


Data.nunique()  # It shows the total no. of unique values in each column. 
# It can be applied on a single column as well as on whole dataframe.


# In[14]:


Data.count()  #  It shows the total no. of non-null values in each column. 
#It can be applied on a single column as well as on whole dataframe.


# In[16]:


Data['Weather'].value_counts()  #In a column, it shows all the unique values with their count. 
# It can be applied on single column only.


# In[17]:


Data.info()   #  Provides basic information about the dataframe.


# 

# In[20]:


Data['Wind Speed_km/h'].unique()   # Q) 1. all the unique 'Wind Speed' values in the data.


# In[30]:


Data.Weather.value_counts() # Q) 2 the number of times when the 'Weather is exactly Clear'.


# In[34]:


# Filtering        
Data[Data.Weather == 'Clear']


# In[35]:


#with  groupby()

Data.groupby('Weather').get_group('Clear')


# In[39]:


Data[Data["Wind Speed_km/h"] == 4] # Q)3 the number of times when the 'Wind Speed was exactly 4 km/h'.


# In[41]:


Data.isnull().sum()  # Q. 4)  all the Null Values in the data.


# In[42]:


Data.notnull()


# In[44]:


Data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


# In[45]:


Data.head(2)   # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.


# In[46]:


Data.Visibility_km.mean()  # Q.6) the mean of 'Visibility' ?


# In[48]:


Data.Press_kPa.std() # Q. 7) Standard Deviation of 'Pressure'  in this data?


# In[49]:


Data['Rel Hum_%'].var() # Q. 8) the Variance of 'Relative Humidity' in this data ?


# In[50]:


# value_counts()    # Q. 9) Find all instances when 'Snow' was recorded.
#data.head(2)
Data['Weather Condition'].value_counts()


# In[52]:


#Filtering
Data[Data['Weather Condition'] == 'Snow']


# In[55]:


# str.contains
Data[Data['Weather Condition'].str.contains('Snow')].tail(20)


# In[59]:


Data.head(2)    # Q. 10)  all instances when 'Wind Speed is above 24' and 'Visibility is 25'.
Data[(Data['Wind Speed_km/h'] > 24) & (Data['Visibility_km'] == 25)]


# In[61]:


Data.groupby('Weather Condition').mean()  
# Q. 11) Mean value of each column against each 'Weather Conditon' ?


# In[64]:


Data.groupby('Weather Condition').min()


# In[63]:


Data.groupby('Weather Condition').max()
# Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Conditon' ?


# In[65]:


Data[(Data['Weather Condition'] == 'Clear') | (Data['Visibility_km'] > 40)].tail(50)
# Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.


# In[67]:


Data.head(3)
Data[(Data['Weather Condition'] == 'Clear') & (Data['Rel Hum_%'] > 50)|(Data['Visibility_km'] > 40)]

# Q. 15)  all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'


# In[ ]:




