#!/usr/bin/env python
# coding: utf-8

# # Covid Impact Analysys by Google Mobilty Data Analysis for City of Toronto
# 
# # Developed by Taslima Parvin, Toronto, Email: rubaparv@gmail.com

# In[1]:


import pandas as pd
import calendar

import plotly.graph_objects as go
import plotly.express as px


# In[2]:


# Read Google Mobility Region-wise Canada Data
df1=pd.read_excel(r'J:\Taslima\data science\2020_CA_Region_Mobility_Report.xlsx')


# In[3]:


# Check Columns
df1.columns


# In[4]:


df1.info()


# In[5]:


# Filter Toronto Area Data
dfT=df1[df1['sub_region_2']=='Toronto']


# In[6]:


# Filter only the date and landuse attributes
dfTOR=dfT[['date',
       'retail_and_recreation_percent_change_from_baseline',
       'grocery_and_pharmacy_percent_change_from_baseline',
       'parks_percent_change_from_baseline',
       'transit_stations_percent_change_from_baseline',
       'workplaces_percent_change_from_baseline',
       'residential_percent_change_from_baseline']]


# In[7]:


# Check if there is any null?
dfTOR.isnull().sum()


# In[8]:


# Convert data time to Pandas date time format
dfTOR['DateTime']=pd.to_datetime(dfTOR['date'])
# another option: df['DateTime'] = pd.to_datetime(df['Start Time'], format = '%d/%m/%Y %H:%M:%S')


# In[9]:


# Get day of the week (0=mon day), date, month hour etc
dfTOR['Year'] =dfTOR.DateTime.dt.year
dfTOR['Month'] =dfTOR.DateTime.dt.month
dfTOR['WeekNo'] =dfTOR.DateTime.dt.week
dfTOR['Weekday'] =dfTOR.DateTime.dt.weekday
dfTOR['DayOfMonth']  =dfTOR.DateTime.dt.day


# In[10]:


# Check if this is only 202o data or not?
dfTOR['Year'].value_counts()


# In[11]:


# Monthly Average of Each Day of the Week (i.e. same data as each week has only 1 data)
res1=dfTOR.groupby(['Year','Month'])['retail_and_recreation_percent_change_from_baseline',
       'grocery_and_pharmacy_percent_change_from_baseline',
       'parks_percent_change_from_baseline',
       'transit_stations_percent_change_from_baseline',
       'workplaces_percent_change_from_baseline',
       'residential_percent_change_from_baseline'].mean()

resultM=res1.reset_index()


# In[12]:


# Weekly Average of Each Day of the Week (i.e. same data as each week has only 1 data)
res2=dfTOR.groupby(['Year','WeekNo'])['retail_and_recreation_percent_change_from_baseline',
       'grocery_and_pharmacy_percent_change_from_baseline',
       'parks_percent_change_from_baseline',
       'transit_stations_percent_change_from_baseline',
       'workplaces_percent_change_from_baseline',
       'residential_percent_change_from_baseline'].mean()

resultW=res2.reset_index()


# In[13]:


# Convert month number to month name
resultM['Month'] = resultM['Month'].apply(lambda x: calendar.month_abbr[x])
resultM


# In[14]:


retMonth=resultM
X1=list(retMonth['Month'])

Y1=list(retMonth['retail_and_recreation_percent_change_from_baseline'])
Y2=list(retMonth['grocery_and_pharmacy_percent_change_from_baseline'])
Y3=list(retMonth['parks_percent_change_from_baseline'])
Y4=list(retMonth['transit_stations_percent_change_from_baseline'])
Y5=list(retMonth['workplaces_percent_change_from_baseline'])
Y6=list(retMonth['residential_percent_change_from_baseline'])


# In[15]:


# Retail and Recreation Daily Percent Change from Baseline

fig = go.Figure([go.Bar(x=dfTOR['DateTime'], y=dfTOR['retail_and_recreation_percent_change_from_baseline'])])

fig.update_layout(xaxis_title="Year 2020",
    yaxis_title="% Change from Pre-Covid Base Level",barmode='group', height=600, width=1000, title_text="Retail and Recreation Daily Percent Change from Baseline")

fig.show()


# In[16]:


# Weekly Time Series with Rangeslider for Retail and Recreation

fig = px.line(resultW, x='WeekNo', y='retail_and_recreation_percent_change_from_baseline', title='Weekly Time Series with Rangeslider for Retail and Recreation')

fig.update_xaxes(rangeslider_visible=True)

fig.update_layout(shapes=[
    # adds line at y=5
    dict(
      type= 'line',
      xref= 'paper', x0= 0, x1= 20,
      yref= 'y', y0= 0, y1= 0,
    )
])

fig.show()


# In[17]:


# Retail and Recreation Monthly Percent Change from Baseline

fig = go.Figure(data=[
    go.Scatter(name='retail_and_recreation', x=X1, y=Y1,fill='tonexty', marker_color='rgba(150, 200, 250, 1)'),
#    go.Scatter(name='retail_and_recreation', x=X1, y=Y1,marker_color='rgba(150, 200, 250, 1)'),   
])



fig.update_layout(xaxis_title="Month of 2020",
    yaxis_title="% Change from Pre-Covid Base Level",barmode='group', height=600, width=800, title_text="Retail and Recreation Monthly Percent Change from Baseline")


fig.show()


# In[18]:


# Grocery and Pharmacy Daily Percent Change from Baseline

fig = go.Figure([go.Bar(x=dfTOR['DateTime'], y=dfTOR['grocery_and_pharmacy_percent_change_from_baseline'])])

fig.update_layout(xaxis_title="Year 2020",
    yaxis_title="% Change from Pre-Covid Base Level",barmode='group', height=600, width=1000, title_text="Grocery and Pharmacy Daily Percent Change from Baseline")

fig.show()


# In[19]:


# Weekly Time Series with Rangeslider for Grocery and Pharmacy


fig = px.line(resultW, x='WeekNo', y='grocery_and_pharmacy_percent_change_from_baseline', title='Weekly Time Series with Rangeslider for Grocery and Pharmacy')

fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[20]:


# Grocery and Pharmacy Monthly Percent Change from Baseline


fig = go.Figure(data=[
    go.Scatter(name='grocery_and_pharmacy', x=X1, y=Y2,fill='tonexty', marker_color='rgba(150, 200, 250, 1)'),
 
])
# Change the bar mode


fig.update_layout(xaxis_title="Month of 2020",
    yaxis_title="% Change from Pre-Covid Base Level", barmode='group', height=600, width=800, title_text="Grocery and Pharmacy Monthly Percent Change from Baseline")


fig.show()


# In[21]:


# Parks Daily Percent Change from Baseline

fig = go.Figure([go.Bar(x=dfTOR['DateTime'], y=dfTOR['parks_percent_change_from_baseline'])])

fig.update_layout(xaxis_title="Year 2020",
    yaxis_title="% Change from Pre-Covid Base Level",barmode='group', height=600, width=1000, title_text="Parks Daily Percent Change from Baseline")

fig.show()


# In[22]:


# Weekly Time Series with Rangeslider for Parks


fig = px.line(resultW, x='WeekNo', y='parks_percent_change_from_baseline', title='Weekly Time Series with Rangeslider for Parks')

fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[23]:


# Parks Monthly Percent Change from Baseline


fig = go.Figure(data=[
    go.Scatter(name='parks', x=X1, y=Y3,fill='tonexty', marker_color='rgba(150, 200, 250, 1)'),
 
])

fig.update_layout(xaxis_title="Month of 2020",
    yaxis_title="% Change from Pre-Covid Base Level", barmode='group', height=600, width=800, title_text="Parks Monthly Percent Change from Baseline")


fig.show()


# In[24]:


# Transit Stations Daily Percent Change from Baseline

fig = go.Figure([go.Bar(x=dfTOR['DateTime'], y=dfTOR['transit_stations_percent_change_from_baseline'])])

fig.update_layout(xaxis_title="Year 2020",
    yaxis_title="% Change from Pre-Covid Base Level",barmode='group', height=600, width=1000, title_text="Transit Stations Daily Percent Change from Baseline")

fig.show()


# In[25]:


# Weekly Time Series with Rangeslider for Transit Stations


fig = px.line(resultW, x='WeekNo', y='transit_stations_percent_change_from_baseline', title='Weekly Time Series with Rangeslider for Transit Stations')

fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[26]:


# Transit Stations Monthly Percent Change from Baseline

fig = go.Figure(data=[
    go.Scatter(name='transit_station', x=X1, y=Y4,fill='tonexty', marker_color='rgba(150, 200, 250, 1)'),])

fig.update_layout(xaxis_title="Month of 2020",
    yaxis_title="% Change from Pre-Covid Base Level", barmode='group', height=600, width=800, title_text="Transit Stations Daily Percent Change from Baseline")


fig.show()


# In[27]:


# Workplaces Daily Percent Change from Baseline

fig = go.Figure([go.Bar(x=dfTOR['DateTime'], y=dfTOR['workplaces_percent_change_from_baseline'])])

fig.update_layout(xaxis_title="Year 2020",
    yaxis_title="% Change from Pre-Covid Base Level",barmode='group', height=600, width=1000, title_text="Workplaces Daily Percent Change from Baseline")

fig.show()


# In[28]:


# Weekly Time Series with Rangeslider for Workplaces


fig = px.line(resultW, x='WeekNo', y='workplaces_percent_change_from_baseline', title='Weekly Time Series with Rangeslider for Work Places')

fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[29]:


# Workplaces Monthly Percent Change from Baseline

fig = go.Figure(data=[
    go.Scatter(name='workplaces_percent_change_from_baseline', x=X1, y=Y5,fill='tonexty', marker_color='rgba(150, 200, 250, 1)'),
 
])


fig.update_layout(xaxis_title="Month of 2020",
    yaxis_title="% Change from Pre-Covid Base Level", barmode='group', height=600, width=800, title_text="Workplaces Monthly Percent Change from Baseline")


fig.show()


# In[30]:


# Residential Daily Percent Change from Baseline

fig = go.Figure([go.Bar(x=dfTOR['DateTime'], y=dfTOR['residential_percent_change_from_baseline'])])

fig.update_layout(xaxis_title="Year 2020",
    yaxis_title="% Change from Pre-Covid Base Level",barmode='group', height=600, width=1000, title_text="Residential Daily Percent Change from Baseline")

fig.show()


# In[31]:


# Weekly Time Series with Rangeslider for Residential

fig = px.line(resultW, x='WeekNo', y='residential_percent_change_from_baseline', title='Weekly Time Series with Rangeslider for Residential')

fig.update_xaxes(rangeslider_visible=True)
fig.show()


# In[32]:


# Residential Monthly Percent Change from Baseline

fig = go.Figure(data=[
    go.Scatter(name='residential_percent_change_from_baseline', x=X1, y=Y6,fill='tonexty', marker_color='rgba(150, 200, 250, 1)'),
 
])


fig.update_layout(xaxis_title="Month of 2020",
    yaxis_title="% Change from Pre-Covid Base Level", barmode='group', height=600, width=800, title_text="Residential Monthly Percent Change from Baseline")


fig.show()


# In[ ]:





# In[ ]:





# In[ ]:




