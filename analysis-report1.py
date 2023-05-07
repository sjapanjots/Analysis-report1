#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[7]:


#EDA (exploratry data anylysis ) and data cleaning 


# In[9]:


df = pd.read_csv('C:\data anyliss\hotel_bookings 2.csv')


# In[10]:


df.head()


# In[11]:


df.tail()


# In[13]:


df.shape


# In[14]:


df.columns


# In[15]:


df.info


# In[16]:


df.info()


# In[17]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[18]:


df.info()


# In[19]:


df.describe(include = 'object')


# In[21]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[22]:


df.isnull().sum()


# In[25]:


df.drop(['company','agent'], axis = 1, inplace = True)
df.dropna(inplace = True)


# In[27]:


df.isnull().sum()


# In[28]:


df.dropna(inplace = True)


# In[30]:


df.isnull().sum()


# In[31]:


df.describe()


# In[32]:


df['adr'].plot(kind = 'box')


# In[33]:


df = df[df['adr']<5000]


# In[34]:


df.describe()


# In[37]:


#Data Analysis and Visualization 


# In[44]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)
plt.figure(figsize = (5,4))
plt.title('Reservation Status Count')
plt.bar(['Not cancelled','canceled'],df['is_canceled'].value_counts(), edgecolor = 'k', width = 0.7)
plt.show()


# In[52]:


plt.figure(figsize = (8,4))
ax1 = sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_ =ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels' , size =20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled' , 'cenceled'])
plt.show()


# In[53]:


#price of the city hotel and mantainence of the city hotel 


# In[57]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True )


# In[58]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True )


# In[59]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[60]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel' , fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[62]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot( x = 'month' , hue = 'is_canceled' , data = df , palette = 'bright')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation Status Per Month ' , size = 20)
plt.xlabel('Month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[65]:


plt.figure(figsize = (15,8))
plt.title('ADR per Month' , fontsize = 30)
sns.barplot('month', 'adr', data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.legend(fontsize = 20)
plt.show()


# In[68]:


plt.figure(figsize = (15,8))
plt.title('ADR per month' , fontsize = 30)
sns.barplot('month', 'adr', data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.legend(fontsize = 30)
plt.show()


# In[72]:


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('top 10 countaries with reservation canceled ')
plt.pie(top_10_country , autopct = '%.2f',labels = top_10_country.index)
plt.show()


# In[73]:


df['market_segment'].value_counts()


# In[74]:


df['market_segment'].value_counts(normalize = True)


# In[76]:


cancelled_data['market_segment'].value_counts(normalize = True)


# In[86]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date' , inplace = True)

not_cancelled_data = df[df['is_canceled'] ==0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True )
not_cancelled_df_adr.sort_values('reservation_status_date' , inplace = True )

plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'], label = 'not cancelled ')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()


# In[88]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016')&(cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016')&(not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[91]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate' , fontsize = 30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'], label = 'not cancelled ')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend(fontsize = 20)
plt.show()


# In[ ]:




