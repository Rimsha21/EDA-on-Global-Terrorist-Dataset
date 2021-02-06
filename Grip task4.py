
# coding: utf-8

# ## Author- Rimsha Virmani
# 
# ## GRIP @ The Sparks Foundation
# 
# ## Task 3: Perform ‘Exploratory Data Analysis’ on dataset ‘Global Terrorism’
# 
# ## Dataset: https://bit.ly/2TK5Xn5

# In[21]:


#Importing required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#Importing data
df = pd.read_csv('Terrorism.csv',encoding='ISO-8859-1')
df.head()


# In[5]:


df.head()


# In[7]:


df.shape


# In[12]:


#renaming columns for better understanding
df.rename(columns={'iyear':'Year','imonth':'Month','extended':'Extended','iday':'Day','country_txt':'Country',
                  'provstate':'State','region_txt':'Region','attacktype1_txt':'Attacktype','target1':'Target',
                   'nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type',
                   'weaptype1_txt':'Weapon_type','motive':'Motive','city':'City','latitude':'Latitude','longitude':'Longitude'}
          ,inplace=True
                  
                  )


# In[13]:


df.head()


# In[15]:


#deleting the unnecessary columns
df= df[['Year','Month','Extended','Day','Country','State','Region','City','Latitude','Longitude',
                 'Attacktype','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]
df.head()


# In[16]:


df.shape


# In[17]:


#checking for null values
df.isnull().sum()


# In[18]:


corrmat= df.corr()
corrmat


# In[22]:


#plotting heatmap of correlation
plt.figure(figsize=(10,5))
sns.heatmap(corrmat, annot=True)
plt.show()


# ## Top 10 countries with the most terrorist attacks

# In[23]:


df['Country'].value_counts().head(10)


# In[26]:


plt.figure(figsize = (10,5))
sns.barplot(df['Country'].value_counts()[:15].index,df['Country'].value_counts()[:15].values)
plt.title('Top Countries Affected')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation= 90)
plt.show()


# ## Top states with most terrorist attacks

# In[29]:


df['State'].value_counts().head()


# In[31]:


plt.figure(figsize = (10,5))
sns.barplot(df['State'].value_counts()[:15].index,df['State'].value_counts()[:15].values)
plt.title('Top States Affected')
plt.xlabel('States')
plt.xticks(rotation= 90)
plt.ylabel('Count')
plt.show()


# ## Top regions with most terrorist attacks

# In[32]:


df['Region'].value_counts().head()


# In[33]:


plt.figure(figsize = (10,5))
sns.barplot(df['Region'].value_counts()[:15].index,df['Region'].value_counts()[:15].values)
plt.title('Top Regions Affected')
plt.xlabel('Regions')
plt.xticks(rotation= 90)
plt.ylabel('Count')
plt.show()


# ## Top cities with most terrorist attacks

# In[35]:


df['City'].value_counts().head(10)


# In[36]:


plt.figure(figsize = (10,5))
sns.barplot(df['City'].value_counts()[:15].index,df['City'].value_counts()[:15].values)
plt.title('Top Cities Affected')
plt.xlabel('Cities')
plt.xticks(rotation= 90)
plt.ylabel('Count')
plt.show()


# ## Years with most terrorist attacks

# In[37]:


df['Year'].value_counts().head(10)


# In[38]:


plt.figure(figsize = (10,5))
sns.barplot(df['Year'].value_counts()[:15].index,df['Year'].value_counts()[:15].values)
plt.title('Top Years Affected')
plt.xlabel('Year')
plt.xticks(rotation= 90)
plt.ylabel('Count')
plt.show()


# ## Attack type that happened the most

# In[39]:


df['Attacktype'].value_counts()


# In[40]:


plt.figure(figsize = (10,5))
sns.barplot(df['Attacktype'].value_counts()[:15].index,df['Attacktype'].value_counts()[:15].values)
plt.title('Most frequent Attack type')
plt.xlabel('Attack type')
plt.xticks(rotation= 90)
plt.ylabel('Count')
plt.show()


# ## Groups with the most attacks

# In[42]:


df['Group'].value_counts().head(10)


# In[43]:


plt.figure(figsize = (10,5))
sns.barplot(df['Group'].value_counts()[:15].index,df['State'].value_counts()[:15].values)
plt.title('Most frequent Groups involved')
plt.xlabel('Groups involved')
plt.xticks(rotation= 90)
plt.ylabel('Count')
plt.show()


# ## Most used weapon type

# In[44]:


df['Weapon_type'].value_counts().head(10)


# In[47]:


plt.figure(figsize = (10,5))
sns.barplot(df['Weapon_type'].value_counts()[:15].index,df['Weapon_type'].value_counts()[:15].values)
plt.title('Most used Weapon Type')
plt.xlabel('Weapon Type')
plt.xticks(rotation= 90)
plt.ylabel('Count')
plt.show()


# ## Killed vs Wounded 

# In[51]:


#plotting scatter plot 

df.plot(kind='scatter', x='Killed', y='Wounded', alpha=0.5, color='blue', figsize=(10,6))
plt.xlabel('Killed')
plt.ylabel('Wounded')
plt.title('Killed vs Wounded')
plt.show()


# ## Conclusion
# ## Hot zones:
# ## 1. Most affected countries are Iraq, Pakistan and Afghanistan
# ## 2. Most affected State is Baghdad
# ## 3. Most affected year is 2014
# ## 4. The most frequent attack type is Bombing/Explosion
# ## 5.The most used weapon is Explosives.
