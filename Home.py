import streamlit as st
import pandas as pd

# Specify the page layout using streamlit
st.set_page_config(
    layout='wide',
    page_title='Campaign Dashboard',
    page_icon=':bar_chart',
)
st.title('Welcome to Campaign Manager')

# Reads an excel file as a panda Dataframe: 2 dimensional array with labeled rows and columns
df_registered_voters = pd.read_excel(
    io='mauaVoters.xlsx',
    engine='openpyxl',
    sheet_name='maua',
    skiprows=0,
    usecols='A:K',
    # nrows=18,
)
# Read excel list of recruited voters
df_recruited_voters = pd.read_excel(
    io='recruited_voters.xlsx',
    engine='openpyxl',  
    sheet_name='Recruited Voters',
    skiprows=0,
    usecols='A:N',
    # nrows=18,
)

#Get dataframe of voters recruited in the last week
recruitment_dates = pd.read_excel(
    io='recruited_voters.xlsx',
    engine='openpyxl',
    sheet_name='Recruited Voters',
    skiprows=0,
    usecols='D',
    # nrows=18,
)
