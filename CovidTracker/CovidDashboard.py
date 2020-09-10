#!/usr/bin/env python
# coding: utf-8

# In[3]:


from __future__ import print_function


# In[2]:


pip install plotly


# In[4]:


import pandas as pd 


# In[5]:


import numpy as np


# In[6]:


import plotly.express as plty


# In[7]:


import plotly.graph_objects as go


# In[8]:


import folium


# In[9]:


import time


# In[10]:



from ipywidgets import interact, interactive, fixed, interact_manual


# In[11]:


import ipywidgets as widgets


# In[12]:


death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')


# In[13]:


death_df.columns=map(str.lower,death_df.columns)
confirmed_df.columns=map(str.lower,confirmed_df.columns)
recovered_df.columns=map(str.lower,recovered_df.columns)
country_df.columns=map(str.lower,country_df.columns)


# In[14]:


death_df=death_df.rename(columns={'province/state':'state','country/region':'country'})
confirmed_df=confirmed_df.rename(columns={'province/state':'state','country/region':'country'})
recovered_df=recovered_df.rename(columns={'province/state':'state','country/region':'country'})
country_df=country_df.rename(columns={'country_region':'country'})


# In[15]:


sortperworsthit_country_df=country_df.sort_values('confirmed',ascending=False)[['country','last_update','lat','long_','confirmed','deaths','recovered','active','incident_rate']]


# In[16]:


def highlight_column(x):
	m='background-color: red'
	n='background-color: yellow'
	o='background-color: green'
	temp_df=pd.DataFrame('',index=x.index,columns=x.columns)
	temp_df.iloc[:,4]=n
	temp_df.iloc[:,5]=m
	temp_df.iloc[:,6]=o
	return temp_df


# In[17]:


sortperworsthit_country_df.style.apply(highlight_column,axis=None)


# In[18]:


figure=plty.scatter(sortperworsthit_country_df.head(10), x='country',y='confirmed',size='confirmed',color='country',hover_name='country',size_max=60)

figure.show()


# In[19]:


def plot_cases_for_country(country):
    labels=['confirmed','deaths']
    colors=['yellow','red']
    mode_size=[6,8]
    line_size=[4,5]

    df_list=[confirmed_df,death_df]

    fig=go.Figure()

    for i,df in enumerate(df_list):
        if country=='World' or country=='world':
            x_data=np.array(list(df.iloc[:,5:].columns))
            y_data=np.sum(np.asarray(df.iloc[:,5:]),axis=0)
        else:
            x_data=np.array(list(df.iloc[:,5:].columns))
            y_data=np.sum(np.asarray(df[df['country']==country].iloc[:,5:]),axis=0)
        fig.add_trace(go.Scatter(x=x_data,y=y_data,mode='lines+markers',name=labels[i],line=dict(color=colors[i],width=line_size[i]),connectgaps=True,text="total "+str(labels[i])+": "+str(y_data[-1])))
    fig.show()

interact(plot_cases_for_country,country=sortperworsthit_country_df['country']);


# In[20]:


worldmap=folium.Map(location=[11,0],tiles="cartodbpositron",zoom_start=2,max_zoom=6,min_zoom=2)

for i in range(len(confirmed_df)):
    folium.Circle(
    location=[confirmed_df.iloc[i]['lat'], confirmed_df.iloc[i]['long']],
    fill=True, fill_color='grey',radius=(int(np.log(confirmed_df.iloc[i,-1]+1.00001))+0.2)*10000,
    color='red', tooltip="<div style='margin: 0; background-color: black; color: white;'>"+
                    "<h4 style='text-align:center;font-weight: bold'>"+confirmed_df.iloc[i]['country'] + "</h4>"
                    "<hr style='margin:10px;color: white;'>"+
                    "<ul style='color: white;;list-style-type:circle;align-item:left;padding-left:20px;padding-right:20px'>"+
                        "<li>Confirmed: "+str(confirmed_df.iloc[i,-1])+"</li>"+
                        "<li>Deaths:   "+str(death_df.iloc[i,-1])+"</li>"+
                        "<li>Death Rate: "+ str(np.round(death_df.iloc[i,-1]/(confirmed_df.iloc[i,-1]+1.00001)*100,2))+ "</li>"+
                    "</ul></div>",
    ).add_to(worldmap)

worldmap

