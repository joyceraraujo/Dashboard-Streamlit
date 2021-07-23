import pandas as pd
import streamlit as st
import numpy as np 
import plotly.express as px
import datetime
import requests 
import logging


logger = logging.getLogger()


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

print(df.head())





















# file_name = "2021-07-14-prise-rdv-par-reg.csv"

# df = pd.read_csv(file_name)








# print(df.head())
# res = df.pivot_table(index=['date_debut_semaine', 'code_region', 'region'], columns='rang_vaccinal',
#                      values='nb', aggfunc='first').reset_index()

# # print(res.head())    

# res.rename(columns={1: "première", 2: "deuxième"}, inplace= True)       

# # df.loc[df['rang_vaccinal'] ==2, ['nb']]
# # print(df.loc[((df['code_region'] ==27) & (df['date_debut_semaine'] == "2021-01-18")), ['nb']])

# res["deuxième"] = res["deuxième"].replace(np.nan, 0)
# print(res.head())   

# # fig = px.bar(res, x="date_debut_semaine", y=["rang1", "rang2"], barmode='group', height=400)
# # st.plotly_chart(fig)




# # Add a selectbox to the sidebar:
# list_regions = df["region"].unique().tolist()
# df['rang_vaccinal'] = df['rang_vaccinal'].map({1: "Première", 2: "Deuxième"})
# df['date_debut_semaine'] = pd.to_datetime(df['date_debut_semaine'])  
# # df['rang_vaccinal'] = df['rang_vaccinal'].astype(str)
# print(len(list_regions))
# add_selectbox = st.sidebar.selectbox(
#     'Selectionnez votre region',
#     (sorted(list_regions))
# )
# print(add_selectbox)
# # select_df = df.loc[df['region'] == add_selectbox]
# dict_labels = {'date_debut_semaine': "Semaine", 'nb': "Nombre de rendez-vous", 
#         'rang_vaccinal': "Dose"}

# st.title('Données* des rendez-vous pris dans des centres de vaccination contre la COVID-19 - par région')
# # fig = px.bar(select_df, x="date_debut_semaine", y="nb", color = "rang_vaccinal", height=400, labels= dict_labels,barmode='group')
# # st.plotly_chart(fig)
# # st.write("*Les données sont issues des systèmes d’information de Doctolib, Keldoc et Maiia, ces trois sources étant agrégées par le Ministère des solidarités et de la santé. Source:https://www.data.gouv.fr/fr/datasets/donnees-des-rendez-vous-pris-dans-des-centres-de-vaccination-contre-la-covid-19/")




# # Add a slider to the sidebar:
# # add_slider = st.sidebar.slider(
# #     'Selectionnez une plage de dates',
# #     "01/01/2021", "31/01/2021", ("10/01/2021", "15/01/2021")
# # )

# d3 = st.sidebar.date_input("Selectionnez les semaines",  [datetime.date(2021, 1, 1), datetime.date(2021, 12, 31)])
# if len(d3) >1:
#     select_df = df.loc[(df['region'] == add_selectbox) & (df['date_debut_semaine'].dt.date > d3[0]) & (df['date_debut_semaine'].dt.date <= d3[1])]
#     fig = px.bar(select_df, x="date_debut_semaine", y="nb", color = "rang_vaccinal", height=400, labels= dict_labels,barmode='group')
#     st.plotly_chart(fig)
#     st.write("*Les données sont issues des systèmes d’information de Doctolib, Keldoc et Maiia, ces trois sources étant agrégées par le Ministère des solidarités et de la santé. Source:https://www.data.gouv.fr/fr/datasets/donnees-des-rendez-vous-pris-dans-des-centres-de-vaccination-contre-la-covid-19/")








# # Add a slider to the sidebar:
# # add_slider = st.sidebar.slider(
# #     'Select a range of dates',
# #     0.0, 100.0, (25.0, 75.0)
# # )











# # st.title('Dashboard')
# # st.write("Data:")

# # """
# # # Dashboard
# # Data  table:
# # """

# # df

# # st.bar_chart(df[["nb","date_debut_semaine"]])