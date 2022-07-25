import streamlit as st
import pandas as pd
from utilities.init_state_session import init_session_state_values


# Specify the page layout using streamlit
st.set_page_config(
    page_title='Campaign Dashboard',
    page_icon=':bar_chart',
    layout="centered",
)
st.title('Welcome to Campaign Manager')

#session state variables
ss = st.session_state
#Initialize state values using custom imported function 
init_session_state_values(ss)
ss


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
