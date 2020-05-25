def covidData():    
    import requests
    import pandas as pd 
    import numpy as np 
    from bs4 import BeautifulSoup

    URL ="https://www.worldometers.info/coronavirus/#countries"

    Page=requests.get(URL).text

    soup=BeautifulSoup(Page,'lxml')

    get_table=soup.find("table",id="main_table_countries_today")

    get_table_elements=get_table.tbody.find_all("tr")

    dict={}
    for i in range(len(get_table_elements)):
        try:
            key= get_table_elements[i].find_all("a",href=True)[0].string
        except:
            key= get_table_elements[i].find_all('td')[0].string

        values=[j.string for j in get_table_elements[i].find_all('td')]

        dict[key] = values

    df=pd.DataFrame(dict).iloc[1:13,:].T

    column_names=["Country","Total Cases","New Cases","Total Deaths","New Deaths","Total Recovered","Active Cases","Serious / Critical","Total Cases per 1M population","Deaths per 1M population","Total Tests","Tests per 1M population"]

    df.columns=column_names

    #df.head()

    df.to_csv("CoronaVirus_Live_Tracking.csv")
    
    print("Data collected...Please check for above csv file name")

covidData()
