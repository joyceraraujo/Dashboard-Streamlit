import pandas as pd
import streamlit as st
import numpy as np 
import plotly.express as px
import datetime
import requests 
import logging


logger = logging.getLogger()

#Function to access url to get csv file
def try_open_csv_file(url):
    try:
        logger.debug("Start getting csv file")
        df = pd.read_csv(url)        
        logger.debug("Finished getting csv file")
        
    except Exception as e:
        logger.error(str(e))    
    return df



url = "https://www.data.gouv.fr/fr/datasets/r/3c3565e5-8e50-482d-b76a-fe07599ab4a0"
df = try_open_csv_file(url)



#Data processing
file_name = "region2020.csv"
df_name_regions = pd.read_csv(file_name,usecols=["reg","ncc"])
print(df_name_regions)
dict_name_regions = pd.Series(df_name_regions.ncc.values,index=df_name_regions.reg).to_dict()

print(dict_name_regions)


#Applying map to better identify region and dose 
df['rang_vaccinal'] = df['rang_vaccinal'].map({1: "Première", 2: "Deuxième"})
df["region"] = df["code_region"].map(dict_name_regions)
df['date_debut_semaine'] = pd.to_datetime(df['date_debut_semaine'])  
list_regions = df["region"].unique().tolist()
if len(list_regions) != 17:
    print("ERROR: le nombre de regions n'est pas correcte")
    print(len(list_regions))

#Streamlit settings

# Add a selectbox to the sidebar:

add_selectbox = st.sidebar.selectbox(
    'Selectionnez votre region',
    (sorted(list_regions))
)
# select_df = df.loc[df['region'] == add_selectbox]
dict_labels = {'date_debut_semaine': "Semaine", 'nb': "Nombre de rendez-vous", 
        'rang_vaccinal': "Dose"}

st.title('Données* des rendez-vous pris dans des centres de vaccination contre la COVID-19 - par région')
# Add a Datetime slider to the sidebar:
d3 = st.sidebar.date_input("Selectionnez les semaines",  [datetime.date(2021, 1, 1), datetime.date(2021, 12, 31)])
if len(d3) >1:
    select_df = df.loc[(df['region'] == add_selectbox) & (df['date_debut_semaine'].dt.date > d3[0]) & (df['date_debut_semaine'].dt.date <= d3[1])]
    fig = px.bar(select_df, x="date_debut_semaine", y="nb", color = "rang_vaccinal", height=400, labels= dict_labels,barmode='group')
    st.plotly_chart(fig)
    st.write("*Les données sont issues des systèmes d’information de Doctolib, Keldoc et Maiia, ces trois sources étant agrégées par le Ministère des solidarités et de la santé. Source:https://www.data.gouv.fr/fr/datasets/donnees-des-rendez-vous-pris-dans-des-centres-de-vaccination-contre-la-covid-19/")










# # st.title('Dashboard')
# # st.write("Data:")

# # """
# # # Dashboard
# # Data  table:
# # """

# # df

# # st.bar_chart(df[["nb","date_debut_semaine"]])

#res = df.pivot_table(index=['date_debut_semaine', 'code_region', 'region'], columns='rang_vaccinal',
#                    values='nb', aggfunc='first').reset_index()
